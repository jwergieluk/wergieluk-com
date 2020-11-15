import numpy
import numpy.random
import pandas
import pandas.plotting
import matplotlib.pyplot as plt
import itertools
import click
import datetime

plt.style.use('ggplot')


def s2(x: numpy.ndarray):
    return x / (1.0 + numpy.abs(x))


def relu(x: numpy.ndarray):
    return numpy.maximum(x, 0.0)


def make_df(x, y):
    y_col_name = 'y'
    data = numpy.hstack([x, y])
    df = pandas.DataFrame(data, columns=[f'x{i}' for i in range(x.shape[1])] + [y_col_name, ],
                          index=pandas.Index(data=range(len(y)), name='id'))
    return df


def plot_scatter_matrix(df: pandas.DataFrame, file_name_prefix: str = '', add_title: bool = True):
    pandas.plotting.scatter_matrix(df, diagonal='kde', alpha=0.2, hist_kwds=dict(bins=50))
    if add_title:
        plt.suptitle(file_name_prefix.replace('_', ' '))
    plt.savefig(file_name_prefix + 'scatter_matrix.png', dpi=250)
    plt.close('all')


@click.command()
@click.option('--x-noise', type=click.STRING, default='normal',
              help='Specify the random noise type to be used ("normal" (default), "t4", "cauchy")')
@click.option('--x-noise-factor', type=click.FLOAT, default=1.0,
              help='Random noise multiplied by this number will be added to the feature vector')
@click.option('--num-samples', type=click.INT, default=5000)
@click.option('--num-features', type=click.INT, default=2)
@click.option('--num-layers', type=click.INT, default=2)
@click.option('--reservoir-dim', type=click.INT, default=0)
@click.option('--binary-target/--no-binary-target', default=False)
@click.option('--seed', type=click.INT, default=0)
@click.option('--output-file', type=click.STRING, default='')
def cli(x_noise: str, x_noise_factor: float, num_samples: int,
        num_features: int, num_layers: int, reservoir_dim: int, binary_target: bool,
        seed: int, output_file: str):

    assert num_samples > 0 and num_features > 0 and seed >= 0
    assert 0 < num_layers < 500

    if seed > 0:
        numpy.random.seed(seed)

    if reservoir_dim == 0:
        reservoir_dim = 2*num_features
    assert num_features < reservoir_dim
    randnn = RandNN(x_noise=x_noise, num_features=num_features, num_layers=num_layers,
                    res_dim=reservoir_dim, noise_factor=x_noise_factor)
    x, y = randnn.sample(num_samples)
    if binary_target:
        y_cutoff = numpy.quantile(y, numpy.random.uniform(0.0, 1.0, 1))
        y = numpy.sign(y - y_cutoff)

    df = make_df(x, y)
    if len(output_file) == 0:
        output_file = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S_')
        output_file += f'{x_noise}_f_{num_features}_l_{num_features}_s_{num_samples}_rd_{reservoir_dim}'
        if seed > 0:
            output_file += f'_seed_{seed}'
        output_file += '.csv'
    df.to_csv(output_file, index=True)
    print(output_file)
    if num_features < 8 and num_samples > 75:
        plot_scatter_matrix(df)


class RandNN:
    def __init__(self, x_noise: str, num_features: int, num_layers: int, res_dim: int,
                 noise_factor: float):
        self.res_dim = res_dim
        self.noise_factor = noise_factor
        assert num_layers > 0
        assert num_features > 0
        self.complexity = num_layers
        self.num_features = num_features
        self.x_noise = x_noise
        self.noise_map = {
            'normal': numpy.random.standard_normal,
            'cauchy': numpy.random.standard_cauchy,
            't4': lambda shape: numpy.random.standard_t(4, size=shape)
        }

        self.wb_x_to_res = (self._rng(self.res_dim, num_features), self._rng(self.res_dim))
        self.wb_res = [(self._rng(self.res_dim, self.res_dim), self._rng(self.res_dim))
                       for _ in range(num_layers)]
        self.wb_res_to_x = (self._rng(num_features, self.res_dim), self._rng(num_features))
        self.wb_res_to_y = (self._rng(1, self.res_dim), self._rng(1))

    def _rng(self, dim1: int, dim2: int = 1):
        return self.noise_map[self.x_noise]((dim1, dim2))

    def add_x_drift(self, factor: float):
        assert factor > 0.0
        w, b = self.wb_res_to_x
        w += self._rng(*w.shape)*factor
        b += self._rng(*b.shape)*factor
        # self.wb_res_to_x = (w, b)

    def add_y_drift(self, factor: float):
        assert factor > 0.0
        w, b = self.wb_res_to_y
        w += self._rng(*w.shape)*factor
        b += self._rng(*b.shape)*factor

    def sample(self, num_samples: int, y_non_linearity=None):
        assert num_samples > 0

        x = self._rng(self.num_features, num_samples)
        w, b = self.wb_x_to_res
        x = s2(numpy.dot(w, x) + b)
        for w, b in self.wb_res:
            x = s2(numpy.dot(w, x) + b)
        w, b = self.wb_res_to_x
        x = numpy.dot(w, x) + b

        x_noisy = x + self._rng(self.num_features, num_samples) * self.noise_factor
        # x = s2(numpy.dot(w, x) + b)

        w, b = self.wb_x_to_res
        y = s2(numpy.dot(w, x_noisy) + b)
        for w, b in self.wb_res:
            y = s2(numpy.dot(w, y) + b)
        w, b = self.wb_res_to_y
        y = numpy.dot(w, y) + b
        # y = s2(numpy.dot(w, y) + b)
        if y_non_linearity is not None:
            y = y_non_linearity(y)
        base = 1e4
        y = (y * base).astype('int64').astype('float')/base
        # y += numpy.repeat(1e-6, len(y))
        # y += numpy.array(list(range(len(y)))).astype('float')/base
        return numpy.transpose(x), numpy.transpose(y)

    def noise_name(self):
        name = f'reservoir_f_{self.num_features}_x_{self.x_noise}'
        name += f'_c_{self.complexity}'
        if self.model_seed is not None:
            name += f'_s_{self.model_seed}'
        return name


def reservoir_architecture_viz():
    num_layers = [1, 2, 5, 7, 10, 25]
    res_dim = [3, 5, 10, 20, 50, 250]

    for nl, rd in itertools.product(num_layers, res_dim):
        reservoir = RandNN('normal', num_features=2, num_layers=nl, res_dim=rd,
                           noise_factor=0.05)

        x_test, y_test = reservoir.sample(10000)
        plot_scatter_matrix(x_test, y_test, f'layers_{nl}_res_dim_{rd}_')


def reservoir_drift_viz():
    reservoir = RandNN('normal', num_features=2, num_layers=2, res_dim=10,
                       noise_factor=0.05)
    x_test, y_test = reservoir.sample(5000)
    xlim = (numpy.min(x_test[:, 0]), numpy.max(x_test[:, 0]))
    ylim = (numpy.min(x_test[:, 1]), numpy.max(x_test[:, 1]))

    for i in range(300):
        reservoir.add_x_drift(0.01)
        x_test, y_test = reservoir.sample(10000)
        df = pandas.DataFrame(x_test, columns=['x0', 'x1'])
        df.plot.scatter(x='x0', y='x1', xlim=xlim, ylim=ylim, alpha=0.5)
        plt.savefig(f'{i:03d}.png', dpi=250)
        plt.close('all')


if __name__ == '__main__':
    numpy.set_printoptions(precision=4)
    cli()
    # reservoir_architecture_viz()

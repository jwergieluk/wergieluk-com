import numpy
import pandas
import matplotlib.pyplot as plt
import matplotlib
import os
import pathlib

plt.style.use('ggplot')


def to_abs(file_name: str):
    script_dir = pathlib.Path(__file__).parent.absolute()
    return os.path.join(script_dir, file_name)


def main():
    df = pandas.read_csv(to_abs('meditation.csv'), header=0)

    plt.figure(figsize=(6, 1.5))
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)) , marker='*',
                     alpha=0.35, s=matplotlib.rcParams['lines.markersize']*20)
    ax = plt.gca()
    ax.get_yaxis().set_ticks([])
    plt.tight_layout()
    plt.savefig(to_abs('x-axis.png'), dpi=150)
    plt.close('all')


if __name__ == '__main__':
    main()


import numpy
import pandas
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches
import os
import pathlib

plt.style.use('ggplot')


def to_abs(file_name: str):
    script_dir = pathlib.Path(__file__).parent.absolute()
    abs_path = os.path.join(script_dir, file_name)
    print(abs_path)
    return abs_path


def main():
    df = pandas.read_csv(to_abs('meditation.csv'), header=0)

    df.plot.area(figsize=(6, 3))
    plt.savefig(to_abs('meditation.png'))

    plt.figure(figsize=(6, 1.5))
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)) , marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize']*20)
    ax = plt.gca()
    ax.get_yaxis().set_ticks([])
    plt.tight_layout()
    plt.savefig(to_abs('x-axis.png'), dpi=150)

    plt.figure(figsize=(6, 1.5))
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)) , marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize']*20)
    plt.ylim((-0.01, 0.02))
    ax = plt.gca()
    range_count = len(list(i for i in df.iloc[:, 0] if 10.0 <= i < 20.0))
    ax.add_patch(matplotlib.patches.Rectangle((10.0, 0.0), 10.0, range_count/1290.0, alpha=0.4))
    # ax.get_yaxis().set_ticks([])
    plt.tight_layout()
    plt.savefig(to_abs('histogram-construction-a.png'), dpi=150)

    histogram_data = {i: len(list(x for x in df.iloc[:, 0] if i <= x < i + 10.0))
                      for i in range(10, 80, 10)}

    plt.figure(figsize=(6, 2.5))
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)), marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize'] * 20)
    plt.ylim((-0.01, 0.06))
    ax = plt.gca()
    for x0, h in histogram_data.items():
        ax.add_patch(matplotlib.patches.Rectangle((x0, 0.0), 10.0, h / 1290.0, alpha=0.4))
    plt.tight_layout()
    plt.savefig(to_abs('histogram-construction-b.png'), dpi=150)

    plt.close('all')


if __name__ == '__main__':
    main()


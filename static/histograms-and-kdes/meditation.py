from typing import Sequence
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

def get_histogram_data(data: Sequence, interval_len: int):
    histogram_data = {i: len(list(x for x in data if i <= x < i + interval_len))/ (len(data)*interval_len)
                      for i in range(10, 70, int(interval_len))}
    return histogram_data


def histograms(df: pandas.DataFrame):
    data = df.values.reshape((-1, )).tolist()

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

    interval_len = 10.0
    histogram_data = get_histogram_data(data, interval_len)

    plt.figure(figsize=(6, 2.5))
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)), marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize'] * 20)
    plt.ylim((-0.01, 0.06))
    ax = plt.gca()
    for x0, h in histogram_data.items():
        ax.add_patch(matplotlib.patches.Rectangle((x0, 0.0), interval_len, h, alpha=0.4))
    plt.tight_layout()
    plt.savefig(to_abs('histogram-construction-b.png'), dpi=150)

    ax.add_patch(matplotlib.patches.Rectangle((25.0, 0.0), 10.0, histogram_data[20], alpha=1.0))
    ax.add_patch(matplotlib.patches.Rectangle((30.0, 0.0), 5.0, histogram_data[30], alpha=1.0))
    plt.savefig(to_abs('histogram-construction-c.png'), dpi=150)

    print(5.0 * (histogram_data[20] + histogram_data[30]))
    print(len(list(x for x in data if 50.0 <= x))/len(data))

    interval_len = 1.0
    histogram_data = get_histogram_data(data, interval_len)

    plt.figure(figsize=(6, 2.5))
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)), marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize'] * 5)
    plt.ylim((-0.01, 0.2))
    ax = plt.gca()
    for x0, h in histogram_data.items():
        ax.add_patch(matplotlib.patches.Rectangle((x0, 0.0), interval_len, h, alpha=0.4))
    plt.tight_layout()
    plt.savefig(to_abs('histogram-construction-d.png'), dpi=150)

    plt.close('all')


def kdes(df: pandas.DataFrame):
    data = df.values.reshape((-1, )).tolist()

    plt.figure(figsize=(6, 2.5))
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)), marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize'] * 20)
    plt.ylim((-0.01, 0.06))
    ax = plt.gca()
    for x0, h in histogram_data.items():
        ax.add_patch(matplotlib.patches.Rectangle((x0, 0.0), interval_len, h, alpha=0.4))
    plt.tight_layout()
    plt.savefig(to_abs('histogram-construction-b.png'), dpi=150)
    pass


if __name__ == '__main__':
    df = pandas.read_csv(to_abs('meditation.csv'), header=0)
    histograms(df)
    kdes(df)


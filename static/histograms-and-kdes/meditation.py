from typing import Sequence
import numpy
import pandas
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches
import os
import pathlib

plt.style.use('ggplot')
DPI = 250 
FIGURE_SIZE = (6.0, 2.5)


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

    df.plot.area(figsize=FIGURE_SIZE, alpha=0.7)
    plt.savefig(to_abs('meditation.png'), dpi=DPI)

    plt.figure(figsize=(6, 1.5))
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)) , marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize']*20)
    ax = plt.gca()
    ax.get_yaxis().set_ticks([])
    plt.tight_layout()
    plt.savefig(to_abs('x-axis.png'), dpi=DPI)

    plt.figure(figsize=(6, 1.5))
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)) , marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize']*20)
    plt.ylim((-0.01, 0.02))
    ax = plt.gca()
    range_count = len(list(i for i in df.iloc[:, 0] if 10.0 <= i < 20.0))
    ax.add_patch(matplotlib.patches.Rectangle((10.0, 0.0), 10.0, range_count/1290.0, alpha=0.4))
    # ax.get_yaxis().set_ticks([])
    plt.tight_layout()
    plt.savefig(to_abs('histogram-construction-a.png'), dpi=DPI)

    interval_len = 10.0
    histogram_data = get_histogram_data(data, interval_len)

    plt.figure(figsize=FIGURE_SIZE)
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)), marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize'] * 20)
    plt.ylim((-0.01, 0.06))
    ax = plt.gca()
    for x0, h in histogram_data.items():
        ax.add_patch(matplotlib.patches.Rectangle((x0, 0.0), interval_len, h, alpha=0.4))
    plt.tight_layout()
    plt.savefig(to_abs('histogram-construction-b.png'), dpi=DPI)

    ax.add_patch(matplotlib.patches.Rectangle((25.0, 0.0), 10.0, histogram_data[20], alpha=1.0))
    ax.add_patch(matplotlib.patches.Rectangle((30.0, 0.0), 5.0, histogram_data[30], alpha=1.0))
    plt.savefig(to_abs('histogram-construction-c.png'), dpi=DPI)

    print(5.0 * (histogram_data[20] + histogram_data[30]))
    print(len(list(x for x in data if 50.0 <= x))/len(data))

    interval_len = 1.0
    histogram_data = get_histogram_data(data, interval_len)

    plt.figure(figsize=FIGURE_SIZE)
    plt.scatter(x=df.iloc[:, 0], y=numpy.repeat(0.0, len(df)), marker='*',
                alpha=0.35, s=matplotlib.rcParams['lines.markersize'] * 5)
    plt.ylim((-0.01, 0.2))
    ax = plt.gca()
    for x0, h in histogram_data.items():
        ax.add_patch(matplotlib.patches.Rectangle((x0, 0.0), interval_len, h, alpha=0.4))
    plt.tight_layout()
    plt.savefig(to_abs('histogram-construction-d.png'), dpi=DPI)

    plt.close('all')


def epanechnikov_kernel(x, h: float = 1.0):
    return numpy.maximum(0.0, 0.75*(1.0 - numpy.square(x/h))/h)


def box_kernel(x, h: float = 1.0):
    return numpy.maximum(0.0, numpy.sign(0.5 - numpy.abs(x/h))/h)


def kde(x: numpy.ndarray, data, h: float = 1.0, kernel_func = epanechnikov_kernel):
    n = len(data)
    y = numpy.zeros(x.shape)
    for x0 in data:
        y += kernel_func(x - x0, h)
    return y/n

def kdes(df: pandas.DataFrame):
    data = df.values.reshape((-1, )).tolist()
    bandwidth = 1.06*df.std().values[0]/numpy.power(len(df), 1.0/5.0)

    x = numpy.arange(-1.5, 1.5, 0.01)
    fig, ax = plt.subplots(1, 1, figsize=FIGURE_SIZE)
    ax.fill_between(x, 0.0, epanechnikov_kernel(x), alpha=0.4, facecolor='r')
    plt.savefig(to_abs('epanechnikov_kernel_a.png'), dpi=DPI)

    fig, ax = plt.subplots(1, 1, figsize=FIGURE_SIZE)
    ax.fill_between(x, 0.0, box_kernel(x), alpha=0.4, facecolor='r')
    plt.savefig(to_abs('box_kernel.png'), dpi=DPI)

    x = numpy.arange(-0.5, 5.0, 0.01)
    fig, ax = plt.subplots(1, 1, figsize=FIGURE_SIZE)
    ax.fill_between(x, 0.0, epanechnikov_kernel(x - 1.0), alpha=0.4, facecolor='r')
    ax.fill_between(x, 0.0, epanechnikov_kernel(x - 2.0), alpha=0.4, facecolor='r')
    plt.savefig(to_abs('epanechnikov_kernel_b.png'), dpi=DPI)

    x = numpy.arange(-3.5, 3.5, 0.01)
    fig, ax = plt.subplots(1, 1, figsize=FIGURE_SIZE)
    ax.fill_between(x, 0.0, epanechnikov_kernel(x), alpha=0.4, facecolor='r')
    ax.fill_between(x, 0.0, epanechnikov_kernel(x, 2.0), alpha=0.4, facecolor='r')
    ax.fill_between(x, 0.0, epanechnikov_kernel(x, 3.0), alpha=0.4, facecolor='r')
    plt.savefig(to_abs('epanechnikov_kernel_c.png'), dpi=DPI)

    x0 = 50.389
    x = numpy.arange(48.0, 53.0, 0.01)
    fig, ax = plt.subplots(1, 1, figsize=FIGURE_SIZE)
    ax.fill_between(x, 0.0, epanechnikov_kernel(x - x0), alpha=0.5, facecolor='r')
    plt.savefig(to_abs('kde_a.png'), dpi=DPI)

    x = numpy.arange(0.0, 80.0, 0.01)
    fig, ax = plt.subplots(1, 1, figsize=FIGURE_SIZE)
    ax.fill_between(x, 0.0, kde(x, data, bandwidth), alpha=0.5, facecolor='r')
    plt.savefig(to_abs('kde_b.png'), dpi=DPI)

    x = numpy.arange(0.0, 80.0, 0.01)
    fig, ax = plt.subplots(1, 1, figsize=FIGURE_SIZE)
    ax.fill_between(x, 0.0, kde(x, data, bandwidth, box_kernel), alpha=0.5, facecolor='r')
    plt.savefig(to_abs('kde_c.png'), dpi=DPI)
    plt.close('all')

def histograms_and_kdes_with_pandas(df: pandas.DataFrame):
    df.plot.density(figsize=FIGURE_SIZE, alpha=0.7)
    plt.savefig(to_abs('pandas_kde.png'), dpi=DPI)

    df.hist(figsize=FIGURE_SIZE, alpha=0.7)
    plt.savefig(to_abs('pandas_hist.png'), dpi=DPI)
    plt.close('all')


if __name__ == '__main__':
    df = pandas.read_csv(to_abs('meditation.csv'), header=0)
    histograms(df)
    kdes(df)
    histograms_and_kdes_with_pandas(df)


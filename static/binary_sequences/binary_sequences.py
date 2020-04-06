import numpy
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def geom_pmf_plot():
    p = 0.1
    pmf = p * numpy.power(1.0 - p, numpy.arange(0.0, 21, 1.0))
    plt.bar(range(len(pmf)), pmf)
    plt.savefig('geom_pmf.png', dpi=150)


if __name__ == '__main__':
    geom_pmf_plot()


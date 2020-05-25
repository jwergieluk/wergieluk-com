""" Serial dependence in random binary sequences. Julian Wergieluk, 2020. """
import numpy
import pandas
import matplotlib.pyplot as plt
import scipy.optimize
plt.style.use('ggplot')


def meixner_poly_eval(x: numpy.ndarray, max_degree: int, p: float) -> numpy.ndarray:
    """ Evaluates Meixner orthogonal polynomials up to degree d

    :param x: array of points x at which we evaluate M_1(x),..,M_d(x)
    :param max_degree: maximal polynomial degree d
    :param p: success probability

    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.404.3188&rep=rep1&type=pdf
    """

    assert max_degree > 0
    assert 0.0 < p < 1.0
    assert len(x)

    x = x.reshape((-1, 1))
    m = numpy.ones((len(x), max_degree + 1))

    for j in range(max_degree):
        factor_j = ((1.0 - p) * (2.0 * j + 1.0) + p * (j - x + 1.0)) / (
                (j + 1.0) * numpy.sqrt(1.0 - p))
        factor_j_1 = j / (j + 1.0)
        m_j = m[:, [j]]
        if j > 0:
            m_j_1 = m[:, [j - 1]] if j > 0 else numpy.zeros((len(x), 1))
            m[:, [j + 1]] = factor_j * m_j - factor_j_1 * m_j_1
        else:
            m[:, [j + 1]] = factor_j * m_j
    return m


def calc_nonzeros_dist(x: numpy.ndarray) -> numpy.ndarray:
    """ For a given array, calculate the distances between non-zeros.

    Example: [0, 1, 1, 0, 0, 1, 0, 0] -> [1, 3]
    """

    assert len(x) > 0
    x = x.reshape((-1,))
    nonzero_indexes = numpy.where(x > 0.0)[0]
    if len(nonzero_indexes) < 2:
        return numpy.array([])

    return nonzero_indexes[1:] - nonzero_indexes[:-1]


def test_nonzeros_dist():
    a = numpy.array([0, 1, 1, 0, 0, 1, 0, 0])
    numpy.testing.assert_array_equal(numpy.array([1, 3]), calc_nonzeros_dist(a))


def gen_self_exciting_bernoulli(n: int, p1: float, p2: float, size: int = 1):
    assert 0.0 < p1 < 1.0
    x = numpy.zeros((n, size))

    for j in range(size):
        p_local = p1
        for i in range(n):
            x[i, j] = numpy.random.binomial(1, p_local, 1)
            if x[i, j] > 0.0:
                p_local = p2
            else:
                p_local = p1
    return x


def self_exciting_bernoulli_experiment():
    p1 = 0.04
    p2 = 0.24
    x = gen_self_exciting_bernoulli(1000000, p1, p2, 1)
    print('Mean: ', x.mean())


def calc_unconditional_dist():
    p0 = 0.05
    p1 = 0.02

    def error_f(p2: float, disp: bool = False):
        transition_matrix = numpy.array([[1-p1, p1],
                                         [1 - p2, p2]])
        initial_dist = numpy.array([1-p0, p0]).reshape((1, -1))
        tmn = numpy.eye(2)
        for i in range(18):
            tmn = numpy.dot(tmn, transition_matrix)
            pn = numpy.dot(initial_dist, tmn)
            pn = pn.reshape((-1, ))
            if disp:
                print(pn[0], pn[1])
        return abs(pn[1] - p0)

    options = {'maxiter': 100, 'disp': False}
    result = scipy.optimize.minimize(error_f, numpy.array([0.1, ]),
                                     method='L-BFGS-B',
                                     bounds=[(0.0, 1.0)],
                                     options=options)
    print(result)
    p2 = result.x
    error_f(p2, disp=True)


def markov_chain_experiment():
    n = 1000
    meixner_max_degree = 9

    no_mc_samples = 5000
    j_cc_scores = numpy.zeros((no_mc_samples, meixner_max_degree))

    for p1, p2 in ((0.05, 0.05), (0.04, 0.24), (0.03, 0.43), (0.02, 0.62)):
        for i in range(no_mc_samples):
            event_indicators = gen_self_exciting_bernoulli(n, p1, p2, size=1)

            #df = pandas.DataFrame(data=event_indicators).cumsum()
            #plt.figure()
            #df.plot(legend=False)
            #plt.savefig('bubu.png')

            event_dists = calc_nonzeros_dist(event_indicators)
            m = meixner_poly_eval(event_dists, meixner_max_degree, p1)
            j_cc_scores[i, :] = numpy.clip(m.mean(axis=0).reshape((-1, ))[1:], a_min=-1.0, a_max=1.0)

        df = pandas.DataFrame(data=j_cc_scores,
                              columns=[f'E[M_{k}]' for k in range(1, meixner_max_degree+1)])
        plt.figure()
        df.hist(bins=75)
        plt.tight_layout()
        plt.savefig(f'j_cc_hist_{p1}.png')
        print(p1, p2, numpy.abs(j_cc_scores).mean())


def plot_geometric_pmf():
    p = 0.1
    pmf = p * numpy.power(1.0 - p, numpy.arange(1.0, 15, 1.0))
    plt.bar(range(1, len(pmf) + 1), pmf)
    plt.savefig('geom_pmf.png', dpi=150)
    plt.close('all')


def plot_some_meixner_polynomials():
    p = 0.1
    x = numpy.arange(1.0, 100.0, 0.05)
    m = meixner_poly_eval(x, 55, p)
    plt.plot(x, m)
    plt.savefig('meixner_polynomials2.png', dpi=150)
    plt.close('all')


if __name__ == '__main__':
    # self_exciting_bernoulli_experiment()
    # calc_unconditional_dist()
    # plot_geometric_pmf()
    plot_some_meixner_polynomials()
    # markov_chain_experiment()

from typing import Sequence
import numpy as np
import pandas as pd
import scipy.optimize
import scipy.stats
import matplotlib.pyplot as plt


def b1_square(x_view: np.ndarray) -> np.ndarray:
    return np.square(x_view[-1, :])


def b1(sigma_view: np.ndarray) -> np.ndarray:
    return sigma_view[-1, :]


def loglik(ret: np.ndarray, params: Sequence, vola_ret_features=b1_square, vola_sigma_features=b1):
    """ Calculate the likelihood of a process path """
    ret = ret.reshape((-1, 1))
    gamma_0, gamma_1, lambda_1 = params
    sigma_squared = np.repeat(gamma_0, len(ret)).reshape(ret.shape)
    sigma_squared[0, 0] = gamma_0

    for s in range(1, len(ret)):
        sigma_squared[s, :] = gamma_0 + \
                              np.dot(gamma_1, vola_ret_features(ret[0:s, :])) + \
                              np.dot(lambda_1, vola_sigma_features(sigma_squared[0:s, :]))

    return np.sum(scipy.stats.norm.logpdf(ret[1:, 0], loc=0.0, scale=np.sqrt(sigma_squared[1:, 0])))


def mle(ret: np.ndarray, start_params: Sequence):
    """ Maximum-likelihood estimator """

    def error_fuc(theta):
        return -loglik(ret, theta)

    start_params = np.array(start_params)
    result = scipy.optimize.minimize(error_fuc, start_params, method='L-BFGS-B',
                                     bounds=[(1e-8, 1.0), (1e-8, 1.0), (1e-8, 1.0)],
                                     options={'maxiter': 250, 'disp': False})
    return result


def path(no_paths: int, t: int, params: Sequence, vola_ret_features=b1_square, vola_sigma_features=b1):
    """ Simulate process paths """
    assert no_paths > 0 and t > 0
    assert len(params) == 3

    ret = np.random.randn(t, no_paths)
    gamma_0, gamma_1, lambda_1 = params
    gamma_0 = np.repeat(gamma_0, no_paths).reshape((1, no_paths))
    sigma_squared = np.zeros((t, no_paths))
    sigma_squared[0, :] = gamma_0
    ret[0, :] = 0.0

    for s in range(1, t):
        sigma_squared[s, :] = gamma_0 + \
                              np.dot(gamma_1, vola_ret_features(ret[0:s, :])) + \
                              np.dot(lambda_1, vola_sigma_features(sigma_squared[0:s, :]))
        ret[s, :] = ret[s, :] * np.sqrt(sigma_squared[s, :])

    return ret, np.sqrt(sigma_squared)


def noise_from_path(ret: np.ndarray, params: Sequence,
                    vola_ret_features=b1_square, vola_sigma_features=b1) -> np.ndarray:
    """ Extract the noise process path from a GARCH path given a parameter set """
    ret = ret.reshape((-1, 1))
    gamma_0, gamma_1, lambda_1 = params
    sigma_squared = np.repeat(gamma_0, len(ret)).reshape(ret.shape)
    sigma_squared[0, 0] = gamma_0
    noise = np.zeros(ret.shape)

    noise[0, :] = ret[0, :] / np.sqrt(sigma_squared[0, :])
    for s in range(1, len(ret)):
        sigma_squared[s, :] = gamma_0 + \
                              np.dot(gamma_1, vola_ret_features(ret[0:s, :])) + \
                              np.dot(lambda_1, vola_sigma_features(sigma_squared[0:s, :]))
        noise[s, :] = ret[s, :] / np.sqrt(sigma_squared[s, :])
    return noise


def plot_path():
    t = 500
    ret, sigma = path(1, t, [0.001, 0.2, 0.25])
    x = np.cumprod(np.exp(ret), axis=0) * np.repeat(5.0, t).reshape((1, -1))

    fig, ax = plt.subplots(2, 1, figsize=(9, 6))
    ax[0].grid(True)
    ax[0].plot(x, color='b', alpha=0.7)
    ax[0].set_ylabel('Y')
    ax[1].grid(True)
    ax[1].plot(sigma, color='r', alpha=0.7)
    ax[1].set_ylabel('sigma')
    fig.tight_layout()
    fig.savefig('garch-simulation.png')
    plt.close('all')


def plot_hist():
    params = [0.001, 0.2, 0.25]
    n, t = 5000, 100
    ret, sigma = path(n, t, params)
    x = np.cumprod(np.exp(ret), axis=0) * np.repeat(5.0, n).reshape((1, -1))
    print(np.mean(x[25, :]), np.std(x[25, :]))
    save_hist(x[25, :], 'garch-histogram.png')


def save_hist(a: np.ndarray, file_name: str, title=None):
    fig, ax = plt.subplots(1, 1, figsize=(9, 6))
    plt.hist(a, bins=100, density=True, color='b', alpha=0.7)
    if title is not None:
        plt.title(title)
    fig.tight_layout()
    fig.savefig(file_name)
    plt.close('all')


def test_mle_moments1():
    """ Test MLE and show that the moments are recovered quite accurately """

    t = 10000
    params = [0.001, 0.2, 0.25]

    estimated_params = []
    means, stdevs = [], []

    for _ in range(2500):
        ret, sigma = path(1, t, params)
        result = mle(ret, [0.01, 0.01, 0.01])

        estimated_params.append(result.x)
        n, t = 5000, 100
        ret_sim, _ = path(n, t, estimated_params[-1])
        x = np.cumprod(np.exp(ret_sim), axis=0) * np.repeat(5.0, n).reshape((1, -1))
        means.append(np.mean(x[25, :]))
        stdevs.append(np.std(x[25, :]))
        print(np.mean(x[25, :]), np.std(x[25, :]), result.x[0], result.x[1], result.x[2])

    estimated_params = np.vstack(estimated_params)
    means = np.array(means)
    stdevs = np.array(stdevs)

    np.savez_compressed('mc-test-data.npz', means=means, stdevs=stdevs, estimated_params=estimated_params)


def test_mle_moments2():
    data = np.load('mc-test-data.npz')
    means, stdevs, estimated_params = data['means'], data['stdevs'], data['estimated_params']

    fig, ax = plt.subplots(1, 2, figsize=(9, 3))
    ax[0].grid(True)
    ax[0].hist(means, bins=100, density=True, color='b', alpha=0.7)
    ax[0].set_title('mean')
    ax[1].grid(True)
    ax[1].hist(stdevs, bins=100, density=True, color='b', alpha=0.7)
    ax[1].set_title('stdev')
    fig.tight_layout()
    fig.savefig('hist-mean-stdev.png')
    plt.close('all')

    fig, ax = plt.subplots(1, 3, figsize=(9, 3))
    ax[0].grid(True)
    ax[0].set_title('gamma0')
    ax[0].hist(estimated_params[:, 0], bins=50, density=True, color='b', alpha=0.7)

    ax[1].grid(True)
    ax[1].set_title('gamma1')
    ax[1].hist(estimated_params[:, 1], bins=50, density=True, color='b', alpha=0.7)

    ax[2].grid(True)
    ax[2].set_title('lambda1')
    ax[2].hist(estimated_params[:, 2], bins=50, density=True, color='b', alpha=0.7)

    fig.tight_layout()
    fig.savefig('hist-params.png')
    plt.close('all')

    save_hist(means, 'hist-mean.png', 'Mean')
    save_hist(stdevs, 'hist-stdev.png', 'Stdev')
    save_hist(estimated_params[:, 0], 'hist-gamma0.png', 'gamma0')
    save_hist(estimated_params[:, 1], 'hist-gamma1.png', 'gamma1')
    save_hist(estimated_params[:, 2], 'hist-lambda1.png', 'lambda1')


def test_extract_noise():
    """ Extract noise from a path and show that it has a distribution with mean 0 and std 1 """
    params = [0.001, 0.2, 0.25]
    ret, sigma = path(1, 5000, params)
    noise = noise_from_path(ret, params)
    df = pd.DataFrame(noise)
    print(df.describe())


def gold_and_platinum():
    df_gold = pd.read_csv('LBMA-GOLD.csv', parse_dates=True, index_col=0)
    df_platinum = pd.read_csv('LPPM-PLAT.csv', parse_dates=True, index_col=0)

    df: pd.DataFrame = pd.concat([df_gold['USD (PM)'], df_platinum['USD PM']], axis=1, join_axes=[df_platinum.index])
    df.columns = ['XAUUSD', 'XPTUSD']
    df = np.log(df.dropna().sort_index()).diff().dropna()

    X = df['XAUUSD'].values.reshape((-1, 1))

    print(X[:-20, 0])


if __name__ == '__main__':
    plt.style.use('ggplot')
    # plot_hist()
    test_mle_moments2()




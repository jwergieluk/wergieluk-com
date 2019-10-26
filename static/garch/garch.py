import numbers
from typing import Union, Sequence
import numpy as np
import pandas as pd
import scipy.optimize
import scipy.stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def loglik(ret: np.ndarray, params: Sequence):
    """ Calculate the (weighted) likelihood of a process path """
    ret = ret.reshape((-1, 1))
    gamma_0, gamma_1, lambda_1 = params
    sigma_squared = np.repeat(gamma_0, len(ret)).reshape(ret.shape)
    sigma_squared[0, 0] = gamma_0

    def vola_ret_features(x_view: np.ndarray) -> np.ndarray:
        return np.square(x_view[-1, :])

    def vola_sigma_features(sigma_view: np.ndarray) -> np.ndarray:
        return sigma_view[-1, :]

    for s in range(1, len(ret)):
        sigma_squared[s, :] = gamma_0 + \
                              np.dot(gamma_1, vola_ret_features(ret[0:s, :])) + \
                              np.dot(lambda_1, vola_sigma_features(sigma_squared[0:s, :]))

    return np.sum(scipy.stats.norm.logpdf(ret[1:, 0], loc=0.0, scale=np.sqrt(sigma_squared[1:, 0])))


def mle(ret: np.ndarray, start_params: Sequence):
    """Maximum-likelihood estimator"""

    def error_fuc(theta):
        return -loglik(ret, theta)

    start_params = np.array(start_params)
    result = scipy.optimize.minimize(error_fuc, start_params, method='L-BFGS-B',
                                     bounds=[(1e-8, None), (1e-8, None), (1e-8, None)],
                                     options={'maxiter': 50, 'disp': False})
    return result


def path(no_paths: int, t: int, params: Sequence):
    """ Simulate log-returns and return process paths """
    assert no_paths > 0 and t > 0
    assert len(params) == 3

    def vola_ret_features(x_view: np.ndarray) -> np.ndarray:
        return np.square(x_view[-1, :])

    def vola_sigma_features(sigma_view: np.ndarray) -> np.ndarray:
        return sigma_view[-1, :]

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


def noise_from_path(ret: np.ndarray, params: Sequence) -> np.ndarray:
    ret = ret.reshape((-1, 1))
    gamma_0, gamma_1, lambda_1 = params
    sigma_squared = np.repeat(gamma_0, len(ret)).reshape(ret.shape)
    sigma_squared[0, 0] = gamma_0
    noise = np.zeros(ret.shape)

    def vola_ret_features(x_view: np.ndarray) -> np.ndarray:
        return np.square(x_view[-1, :])

    def vola_sigma_features(sigma_view: np.ndarray) -> np.ndarray:
        return sigma_view[-1, :]

    noise[0, :] = ret[0, :] / np.sqrt(sigma_squared[0, :])
    for s in range(1, len(ret)):
        sigma_squared[s, :] = gamma_0 + \
                              np.dot(gamma_1, vola_ret_features(ret[0:s, :])) + \
                              np.dot(lambda_1, vola_sigma_features(sigma_squared[0:s, :]))
        noise[s, :] = ret[s, :] / np.sqrt(sigma_squared[s, :])
    return noise


def plot_path():
    n = 500
    ret, sigma = path(1, n, [0.001, 0.2, 0.25])
    x = np.cumprod(np.exp(ret), axis=0) * np.repeat(5.0, n).reshape((1, -1))

    fig, ax = plt.subplots(2, 1, figsize=(9, 6))
    ax[0].grid(True)
    ax[0].plot(x, color='b', alpha=0.7)
    ax[0].set_ylabel('Y')
    ax[1].grid(True)
    ax[1].plot(sigma, color='r', alpha=0.7)
    ax[1].set_ylabel('sigma')
    fig.tight_layout()
    fig.savefig('garch_1_1-simulation.png')
    plt.close('all')


def plot_hist():
    params = [0.001, 0.2, 0.25]
    x, sigma = path(5, 500, params)
    print(x)


def test_mle():
    params = [0.001, 0.2, 0.25]
    ret, sigma = path(1, 5000, params)

    result = mle(ret, [0.01, 0.01, 0.01])
    print(result)

    noise = noise_from_path(ret, params)

    df = pd.DataFrame(noise)
    print(df.describe())

    fig, ax = plt.subplots(1, 1, figsize=(9, 1))
    ax.grid(True)
    ax.plot(noise, color='b', alpha=0.5)
    fig.savefig('noise.png')
    plt.close('all')


def gold_and_platinum():
    df_gold = pd.read_csv('LBMA-GOLD.csv', parse_dates=True, index_col=0)
    df_platinum = pd.read_csv('LPPM-PLAT.csv', parse_dates=True, index_col=0)

    df: pd.DataFrame = pd.concat([df_gold['USD (PM)'], df_platinum['USD PM']], axis=1, join_axes=[df_platinum.index])
    df.columns = ['XAUUSD', 'XPTUSD']
    df = np.log(df.dropna().sort_index()).diff().dropna()

    X = df['XAUUSD'].values.reshape((-1, 1))

    print(X[:-20, 0])


if __name__ == '__main__':
    test_mle()




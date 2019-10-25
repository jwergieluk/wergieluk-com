from typing import Union

import numpy as np
import pandas as pd
import scipy.optimize


def loglik(X: np.ndarray):
    X = X.reshape((-1, 1))
    X = np.hstack([X, np.roll(X, 1)])
    X[0, 1] = 0.0

    return 0.0


def mle(X: np.ndarray):
    #def error_fuc(theta):
    #    return -loglik(t, x, theta[0], theta[1], theta[2])

    #start = np.array(start)
    #result = scipy.optimize.minimize(error_fuc, start, method='L-BFGS-B',
    #                                 bounds=[(1e-6, None), (None, None), (1e-8, None)],
    #                                 options={'maxiter': 500, 'disp': False})
    return 0.0


def path(x0: Union[float, np.ndarray], t: int, params=None):
    """ Simulate log-returns and return cumprod """
    if isinstance(x0, float):
        x0 = np.array([x0, ])
    x0 = x0.reshape((1, -1))
    n = x0.size
    X = np.random.randn(t, n)
    gamma_0, gamma_1, lambda_1 = params
    sigma_squared = np.zeros((t, n))
    sigma_squared[0, :] = gamma_0 * (1.0 + lambda_1)
    X[0, :] = 0.0

    for s in range(1, t):
        sigma_squared[s, :] = gamma_0 + gamma_1 * np.square(X[s-1, :]) + lambda_1 * sigma_squared[s-1, :]
        X[s, :] = X[s, :] * np.sqrt(sigma_squared[s, :])

    return np.cumprod(np.exp(X), axis=0)*x0, np.sqrt(sigma_squared)


def gold_and_platinum():
    df_gold = pd.read_csv('LBMA-GOLD.csv', parse_dates=True, index_col=0)
    df_platinum = pd.read_csv('LPPM-PLAT.csv', parse_dates=True, index_col=0)

    df: pd.DataFrame = pd.concat([df_gold['USD (PM)'], df_platinum['USD PM']], axis=1, join_axes=[df_platinum.index])
    df.columns = ['XAUUSD', 'XPTUSD']
    df = np.log(df.dropna().sort_index()).diff().dropna()

    X = df['XAUUSD'].values.reshape((-1, 1))

    print(X[:-20, 0])


if __name__ == '__main__':
    X, sigma = path(np.repeat(5.0, 3), 5, [0.001, 0.2, 0.25])
    print(X)


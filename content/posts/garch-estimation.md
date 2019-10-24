---
title: "GARCH parameter estimation from scratch"
date: 2019-10-23
draft: true
katex: true
markup: "mmark"
---

# Plan

Intended audience: me.

* Process dynamics definitions. Maximum likelihood estimator derivation.
* Calibration code using pandas and numpy.
* Simulation.

Models:
* ARCH(1,1), GARCH(1,1)
* ARCH(p,q), GARCH(p,q)

Noises:
* Normal
* (Optional) Student-t
* (Optional) Rademacher

# Introduction

$$\global\def\Xpred#1{(X_s)_{s\lt #1}}$$

Let $$\left( \Omega, \mathcal A, \mathcal F, P \right)$$ be a stochastic basis with a complete $$\sigma$$-algebra $$\mathcal A$$ of measurable subsets of $$\Omega$$, a probability measure $$P$$, and a filtration $$\mathcal F = (F_t)_{t=0, 1, \ldots}$$. 

* Non-negative integers $$0, 1, \ldots $$ are used to index time instants.
* For a vector $$Y = (Y_0, Y_1, \ldots, Y_{n-1})$$, set $$Y_{-1} = Y_{n-1}$$, $$Y_{-2} = Y_{n-2}$$, and so on.
* To get the first $$t$$ elements of a sequence $$X$$ we use the notation $$\Xpred{t} = (X_0,\ldots,X_{t-1})$$.

Let's define an autoregressive process as follows:

$$
\begin{aligned}
X_t &= \mu_t + \sigma_t Z_t \\
\mu_t &= \phi_0 + \sum_{i=1}^{p} \phi_i f_i (\Xpred{t}) \\
\sigma_t^2 &= \gamma_0 + \sum_{i=1}^q \gamma_i g_i(\Xpred{t}) + \sum_{i=1}^r \lambda_i h_i((\sigma_s^2)_{s\lt t}). 
\end{aligned}
$$

Ingredients: 

* $$Z$$ is a noise process adapted to $$\mathcal F$$, such that $$Z_t$$ have all expectation zero, a unit variance, and density $$\eta_Z$$.
* $$\phi_i$$ are real numbers and, to avoid trouble, $$\gamma_i, \lambda_i \geq 0$$, and $$g_i, h_i$$ are non-negative valued.
* $$f_i, g_i, h_i$$ are deterministic functions of the process path.

The backward shift operator $$B^j$$, for $$j\geq 0$$, produces a delayed version of an argument process, i.e. $$B^j (X)_t = X_{t-j}$$, if $$t-j \geq 0$$, and $$B^j (X)_t = 0$$, if $$t-j \lt 0$$. For example

$$
B^1(X) = B(X) = (0, X_1, X_2, \ldots).
$$

For convenience we set $$B^1 = B$$ and $$B^j_t (X) = B^j(X)_t$$.

## Special cases

In an _ARCH_ process the volatility has a simplified form: $$\mu \equiv 0$$ and $$\lambda_i = 0$$ for all $$i$$.

_ARCH(1)_ process additionally restricts $$\gamma_i = 0$$ for all $$i \geq 2$$: 
    
$$
\begin{aligned}
X_t &= \sigma_t Z_t \\
\sigma_t^2 &= \gamma_0 + \gamma_1 B_t(X). 
\end{aligned}
$$

For $$t\gt 0$$ this leads to $$X_t = \gamma_0 Z_t + \gamma_1 X_{t-1} Z_t$$.

GARCH process definitions found in textbooks set $$f_i = h_i = B^i_t$$, $$g_i(\Xpred{t}) = B_t(X^2)$$ and $$\mu\equiv 0$$.

GARCH(1, 1) process is quite popular, so let's state it's dynamics explicitly:

$$
\begin{aligned}
X_t &= \sigma_t Z_t \\
\sigma_t^2 &= \gamma_0 + \gamma_1 B_t(X) + \lambda_1 B_t(\sigma^2). 
\end{aligned}
$$

## Maximum-likelihood estimation

If the $$Z$$ noise is a sequence of i.i.d. random variables then the log-likelihood function of the process path is given by

$$
\ln L(\theta; X) = \sum_{s=1}^t \ln \eta_Z \left( \frac{X_t - \mu_t(\theta)}{\sigma_t(\theta)} \right) - \ln \sigma_t(\theta),
$$

where $$\theta = (\phi_i, \gamma_i, \lambda_i)$$, and $$\eta_Z$$ is the density of $$Z$$.

TODO: Derivation of the conditional likelihood product decomposition.





# Links

* https://katex.org/docs/supported.html
* Quantitative Risk Management. Embrechts, Frei, McNeal, 2015.
* Hill, J. B. (2015). Robust estimation and inference for heavy tailed GARCH. Bernoulli, 21(3), 1629–1669. Retrieved from http://projecteuclid.org/euclid.bj/1432732032
* Bauwens, L. (2006). Multivariate GARCH models: a survey. Retrieved from http://onlinelibrary.wiley.com/doi/10.1002/jae.842/pdf
* Silvennoinen, A., & Teräsvirta, T. (2009). Multivariate GARCH models. Handbook of Financial Time Series. Retrieved from http://link.springer.com/chapter/10.1007/978-3-540-71297-8_9
* Aït-Sahalia, Y., & Kimmel, R. (2007). Maximum likelihood estimation of stochastic volatility models. Journal of Financial Economics, 83(2), 413–452. https://doi.org/10.1016/j.jfineco.2005.10.006




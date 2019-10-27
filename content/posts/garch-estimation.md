---
title: "GARCH parameter estimation from scratch"
date: 2019-10-23
draft: true
katex: true
markup: "mmark"
---



# Introduction

$$\global\def\Xpred#1{(X_s)_{s\lt #1}}$$

Let $$\left( \Omega, \mathcal A, \mathcal F, P \right)$$ be a stochastic basis with a complete $$\sigma$$-algebra $$\mathcal A$$ of measurable subsets of $$\Omega$$, a probability measure $$P$$, and a filtration $$\mathcal F = (\mathcal F_t)_{t=0, 1, \ldots}.$$ 

* Non-negative integers $$0, 1, \ldots $$ are used to index time instants.
* For a vector $$Y = (Y_0, Y_1, \ldots, Y_{n-1})$$, set $$Y_{-1} = Y_{n-1}$$, $$Y_{-2} = Y_{n-2}$$, and so on.
* To get the first $$t$$ elements of a sequence $$X$$ we use the notation $$\Xpred{t} = (X_0,\ldots,X_{t-1}).$$

Let's define a discrete stochastic volatility model as follows:

$$
\begin{aligned}
X_t &= \mu_t + \sigma_t Z_t \\
\mu_t &= \phi_0 + \sum_{i=1}^{p} \phi_i f_i (\Xpred{t}) \\
\sigma_t^2 &= \gamma_0 + \sum_{i=1}^q \gamma_i g_i(\Xpred{t}) + \sum_{i=1}^r \lambda_i h_i((\sigma_s^2)_{s\lt t}). 
\end{aligned}
$$

Ingredients: 

* $$Z$$ is a noise process adapted to $$\mathcal F$$, such that $$Z_t$$ are i.i.d. copies of a random variable with density $$\eta_Z.$$
* $$\phi_i$$ are real numbers and, to avoid trouble, $$\gamma_i, \lambda_i \geq 0$$, and $$g_i, h_i$$ are non-negative valued.
* $$f_i, g_i, h_i$$ are deterministic functions of the process path.
* The process $$\mu$$ is often called the drift, whereas $$\sigma$$ is called the volatility of $$X$$. Because $$\sigma$$ is a stochastic process, the autoregressive process as defined above belongs to a large family of stochastic volatility models.
* In case of an i.i.d. sequence $$Z$$ (such that mean and variance of $$Z_t$$ exist), we have $$\mathbb E [X_t | \mathcal F_{t-1}] = \mu_t$$ and $$\operatorname{Var} [X_t | \mathcal F_{t-1}] = \sigma^2_t.$$

The backward shift operator $$B^j$$, for $$j\geq 0$$, produces a delayed version of an argument process, i.e. $$B^j (X)_t = X_{t-j}$$, if $$t-j \geq 0$$, and $$B^j (X)_t = 0$$, if $$t-j \lt 0$$. For example

$$
B^1(X) = B(X) = (0, X_1, X_2, \ldots).
$$

For convenience we set $$B^1 = B$$ and $$B^j_t (X) = B^j(X)_t = X_{t-j}.$$

## Special cases

For all the special cases in the list below, we assume that the functions $$f_i, g_i$$, and $$h_i$$ pick a single element from the history of the argument process, i.e. $$f_i = h_i = B^i_t$$, and $$g_i(\Xpred{t}) = B^j_t(X^2).$$

_GARCH_ process definitions found in textbooks additionally set $$\mu\equiv 0$$.

_GARCH(1, 1)_ process is quite popular, so let's state it's dynamics explicitly:

$$
\begin{aligned}
X_t &= \sigma_t Z_t \\
\sigma_t^2 &= \gamma_0 + \gamma_1 B_t(X^2) + \lambda_1 B_t(\sigma^2). 
\end{aligned}
$$

In an _ARCH_ process, the volatility has the simplified form with $$\lambda_i = 0$$ for all $$i$$, and $$\mu \equiv 0$$.

$$
\begin{aligned}
X_t &= \sigma_t Z_t \\
\sigma_t^2 &= \gamma_0 + \sum_{i=1}^q \gamma_i B^i_t(X^2). 
\end{aligned}
$$

An _ARCH(1)_ process additionally satisfies $$\gamma_i = 0$$ for all $$i \geq 2$$: 
    
$$
\begin{aligned}
X_t &= \sigma_t Z_t \\
\sigma_t^2 &= \gamma_0 + \gamma_1 B_t(X^2). 
\end{aligned}
$$

## Simulation

Discrete stochastic volatility models are typically used to model the log-returns of an observed time-series. Therefore in order to simulate a path of the original time-series we need to simulate log-returns and calculate 
$$Y = Y_0 \prod_{s=0}^t \exp(X_s).$$

A sample path of a GARCH(1,1) process driven by Gaussian noise with parameters $$(\gamma_0, \gamma_1, \lambda_1) = (0.001, 0.2, 0.25).$$

{{< figure src="/garch/garch_1_1-simulation.png" >}}

Note that the $$\sigma$$ process for $$t>0$$ cannot go below the level of $$\sqrt{\gamma_0 (1 + \lambda_1)} \approx 0.0353$$

## Maximum-likelihood estimation

Log-likelihood function of the process path is given by

$$
\ln L(\theta; X) = \sum_{s=1}^t \ln \eta_Z \left( \frac{X_t - \mu_t(\theta)}{\sigma_t(\theta)} \right) - \ln \sigma_t(\theta),
$$

where $$\theta = (\phi_i, \gamma_i, \lambda_i)$$, and $$\eta_Z$$ is the density of $$Z$$.

TODO: Derivation of the conditional likelihood product decomposition.

#### Monte-Carlo simulation

* 2500 repeated simulations and estimations. 
* Used GARCH(1,1) with parameters (0.001, 0.2, 0.25) and Gaussian noise.
* Search ranges for parameters in the optimization procedure restricted to [1e-8, 1].


{{< figure src="/garch/hist-params.png" >}}

{{< figure src="/garch/hist-mean-stdev.png" >}}

# Code

* python implementation is here: `garch.py`.
* Important functions: `path()`, `mle()`, and `noise_from_path()`.

# Summary

Pros:
* Flexible parametrization.
* Simulation and parameter estimation is easy.

Cons:
* Transition densities over many steps not known explicitly, nor there is a cheap method to approximate them. In fact, the only available method to obtain these densities is Monte-Carlo simulation of the process and density estimation.

# Notes

* Driving noise doesn't have to be normalized to mean 0 and variance 1 as long as we consistently use i.i.d. copies of the same random variable. 
* The optimization process (scipy) spawns multiple python processes and seems to run stuff in parallel. Kind of surprising. Maybe worth investigating. 
* Stupid idea: Cauchy driving noise.
* Can we easily calculate the gradient of the likelihood function?
* Idea: Tensorflow implementation with automatic differentiation.

# References and Links

* https://katex.org/docs/supported.html
* McNeil, Alexander J., Rüdiger Frey, and Paul Embrechts. Quantitative risk management. Princeton university press, 2015.

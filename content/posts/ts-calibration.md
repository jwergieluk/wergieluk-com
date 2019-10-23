---
title: "Time series calibration from scratch"
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

Let $$\left( \Omega, \mathcal A, \mathcal F, P \right)$$ be a stochastic basis with a complete $$\sigma$$-algebra $$\mathcal A$$ of measurable subsets of $$\Omega$$, a probability measure $$P$$, and a nice filtration $$\mathcal F = (F_t)_{t=0, 1, \ldots}$$. 

* Non-negative integers $$0, 1, \ldots $$ are used to index time instants.
* For a finite sequence $$Y = (Y_0, Y_1, \ldots, Y_n)$$, set $$Y_{-1} = Y_n$$, $$Y_{-2} = Y_{n-1}$$, and so on.
* To get the first $$t+1$$ elements of a sequence $$X$$ we use the notation $$\Xpred{t} = (X_0,\ldots,X_t)$$.



Let's define an autoregressive process as follows:

$$
\begin{aligned}
X_t &= \mu_t + \sigma_t Z_t \\
\mu_t &= \phi_0 + \sum_{i=1}^{p} \phi_i f_i (\Xpred{t}) \\
\sigma_t^2 &= \gamma_0 + \sum_{i=1}^q \gamma_i g_i(X_{0,\ldots, t-1}) + \sum_{i=1}^r \lambda_i h_i((\sigma_s^2)_{s\lt t}). 
\end{aligned}
$$

Ingredients: 

* $$Z$$ is a noise process adapted to $$\mathcal F$$, such that $$Z_t$$ have all expectation zero and a unit variance.
* $$\phi_i$$ are real numbers and, to avoid trouble, $$\gamma_i, \lambda_i \geq 0$$, and $$g_i, h_i$$ are non-negative valued.
* $$f_i, g_i, h_i$$ are deterministic functions of the process path.

The backward shift operator $$B^j$$, for $$j\geq 0$$, shifts a process $$j$$-steps backwards in time, i.e. 
$$B^j (X)_t = X_{t-j}$$, if $$t-j \geq 0$$, and $$B^j (X)_t = 0$$, if $$t-j \lt 0$$. For example

$$
B^1(X) = B(X) = (0, X_1, X_2, \ldots).
$$

### Special cases

GARCH process definitions found in textbooks set $$f_i = g_i = h_i = B^i$$ and $$\mu\equiv 0$$.

ARCH process: $$\mu \equiv 0$$ and $$\lambda_i = 0$$ for all $$i$$.

ARCH(1) process additionally restricts $$\gamma_i = 0$$ for all $$i \geq 2$$: 
    
$$
\begin{aligned}
X_t &= \sigma_t Z_t \\
\sigma_t^2 &= \gamma_0 + \gamma_1 B(X)_t. 
\end{aligned}
$$

For $$t\gt 0$$ this leads to $$X_t = \gamma_0 Z_t + \gamma_1 X_{t-1} Z_t$$.

GARCH(1, 1) process is quite popular, so let's state it explicitly:

$$
\PredProj{\sigma^2}{t}
$$

$$
\begin{aligned}
X_t &= \sigma_t Z_t \\
\sigma_t^2 &= \gamma_0 + \gamma_1 B(X)_t + \lambda_1 B(\sigma^2)_{t}. 
\end{aligned}
$$


# Links

* https://katex.org/docs/supported.html
* Quantitative Risk Management. Embrechts, Frei, McNeal, 2015.



---
title: "Risk stabilized portfolios (draft)"
date: 2020-04-14
draft: true
katex: true
markup: "mmark"
---

We work with a standard stochastic basis $$(\Omega, \mathcal A, \mathbb F, \mathbb P)$$ with filtration 
$$\mathbb F = (\mathcal F_{t})_{t\in\mathbb N}$$.

For any process $$Z = (Z_t)_{{t\in\mathbb N}}$$, we define the first difference process $$\Delta Z$$
as $$\Delta Z_0\equiv 0,$$ and $$\Delta Z_t = Z_t - Z_{t-1},$$ for $$t>0.$$

Consider an investment universe consisting of $$n$$ numeraires labeled with integers
$$1,..,n$$. We observe positive exchange rate processes

$$X_{ij} =  (X_{t,ij})_{t\in\mathbb N}$$

with $$X_{ii} \equiv 1$$. The matrix valued process $$X$$ has the property 

$$\mathbb P[X_{ij} X_{ji} \leq 1] = 1.$$

The process $$(X_{t, ij})_{t\in\mathbb N}$$ models the price of one unit of the numeraire $$i$$ in units of the 
numeraire $$j.$$

The constant vector $$h\in\mathbb R_+$$ defines the asset allocation in absolute (accounting) terms. 
The value of a portfolio described by $$h$$ in units of the numeraire $$j$$ is given by

$$V_{t,j} = (h^\top X_t)_j.$$

Adopting the accounting view has a the following nice consequence:

$$\Delta V_{t} = h^\top \Delta X_t.$$

The absolute portfolio return is a linear function of the asset returns.

## Normalized exchange rates

Since absolute returns are so convenient, let's think how we can use these as often as possible. 

Let's say, at time $$t=0$$, we hold a portfolio described with the allocation vector $$h.$$
The value of this portfolio, expressed in the numeraire $$j$$ is given by 

$$V_{0, j} = (h^\top X_0)_j = h_1 X_{0, 1j} + ... + h_1 X_{0, nj}.$$

Let's construct a normalized exchange rate process $$\tilde X$$, such that the prices of all assets,
expressed in the units of the numeraire $$j$$, are given by

$$\tilde X_{t, ij} = X_{t, ij} / X_{0, ij},\ i=1,...,n.$$

This has the nice consequence, that 

$$(X_{0, 1j},...,X_{0,nj}) = (1,...,1).$$

If we set 

$$\tilde h = (h_i X_{0,ij})_{i=1,...,n},$$

then 

$$V_{0, j} = \tilde V_{0, j} = (\tilde h^\top \tilde X_{0})_j,$$

i.e. the $$j$$ value of the portfolio at time $$t=0$$ is not affected by the 
normalization. Ideally, we would like to have 

$$V = \tilde V.$$


## Risk stabilization and risk budgeting


## References

 * López de Prado, Marcos, Building Diversified Portfolios that Outperform Out-of-Sample (May 23, 2016). Journal of Portfolio Management, 2016; https://doi.org/10.3905/jpm.2016.42.4.059 Available at SSRN: https://ssrn.com/abstract=2708678 or http://dx.doi.org/10.2139/ssrn.2708678 


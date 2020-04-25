---
title: "Risk stabilized portfolios"
date: 2020-04-14
draft: false
katex: true
markup: "mmark"
---

We work with a standard stochastic basis $$(\Omega, \mathcal A, \mathbb F, \mathbb P)$$ with filtration 
$$\mathbb F = (\mathcal F_{t})_{t\in\mathbb N}$$.

For any process $$Z = (Z_t)_{{t\in\mathbb N}}$$, we define the first difference process $$\Delta Z$$
as $$\Delta Z_0\equiv 0$$, and $$\Delta Z_t = Z_t - Z_{t-1}$$, for $$t>0$$.

Consider an investment universe consisting of $$n$$ numeraires labeled with integers
$$1,..,n$$. We observe positive exchange rate processes

$$X_{ij} =  (X_{t,ij})_{t\in\mathbb N}$$

with $$X_{ii} \equiv 1$$. The matrix valued process $$X$$ has the property 

$$\mathbb P[X_{ij} X_{ji} \leq 1] = 1.$$

The process $$(X_{t, ij})_{t\in\mathbb N}$$ models the price of one unit of the numeraire $$i$$ in units of the 
numeraire $$j$$.

The constant vector $$h\in\mathbb R_+$$ defines the asset allocation in absolute (accounting) terms. 
The value of a portfolio described by $$h$$ in units of the numeraire $$j$$ is given by

$$V_{t,j} = (h^\top X_t)_j.$$

Adopting the accounting view has a the following nice consequence:

$$\Delta V_{t} = h^\top \Delta X_t.$$




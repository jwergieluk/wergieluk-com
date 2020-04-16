---
title: "Risk stabilized portfolios"
date: 2020-04-14
draft: false
katex: true
markup: "mmark"
---

We work with a standard stochastic basis $$(\Omega, \mathcal A, \mathbb F, \mathbb P)$$ with filtration 
$$\mathbb F = (\mathcal F_{t})_{t\in\mathbb N}$$.

Consider an investment universe consisting of $$n$$ numeraires labeled with integers
$$1,..,n$$. We observe positive exchange rate processes

$$X_{i,j} =  (X_{t,i,j})_{t\in\mathbb N}$$

with $$X_{i,i} \equiv 1$$. The matrix valued process $$X$$ has the property 

$$\mathbb P[X_{i,j} X_{j,i} \leq 1] = 1.$$

The process $$(H_t)_{t\in\mathbb N}$$ defines the asset allocation in absolute (accounting) terms.
The observation $$H_{t,1} = 1$$ I have one piece of numeraire $$1$$ in my portfolio. 

The value of a portfolio described by $$H$$ in terms of numeraire $$j$$ is given by

$$V_{t} = H^\top_

The process $$V = (V_t)_{t\geq 0}$$ tracks the value of a portfolio, following the
allocation $$H$$. We have

$$V_t = H^\top_{t-1} X_t$$
 





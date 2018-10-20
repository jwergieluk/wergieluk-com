---
title: "Ornstein-Uhlenbeck calibration"
date: 2018-10-20T13:47:21+02:00
draft: true
katex: true
markup: "mmark"
tags:
    - machine-learning
    - stochastic-processes
---

An Ornstein-Uhlenbeck process taking values in $$\mathbb{R}^{n}$$, $$n\geq 1$$, looks as follows: 

$$ dX_{t} = - A_{t}\left(  X_t - \alpha_{t} \right)dt + v d B_{t}, $$

with a standard $$m$$-dimensional Brownian motion $$B$$, a real $$n\times m$$-matrix
$$v$$, a deterministic real $$n\times n$$ matrix function $$A_t$$, an $$\mathbb{R}^{n}$$
vector function $$\alpha_{t}$$ and a deterministic initial value $$X_{0}$$.

---
title: "Basics of multivariate student t distribution"
date: 2021-01-09
modified: 2021-01-09
draft: false
markup: "mmark"
katex: true
tags:
    - machine-learning
    - probability-theory
---

The density of a (non-degenerate) multivariate normal distribution with zero mean is given by

$$
\frac{1}{\sqrt{(2\pi)^n |\Sigma|}} \exp \Big( -\frac{1}{2} x^\top \Sigma^{-1} x \Big),
$$

where $$\Sigma$$ is a (positive-semidefinite) covariance matrix.

For comparison, the density of the multivariate student t distribution with zero mean is

$$
\frac{\Gamma[(\nu + n)/2]}{\Gamma(\nu/2) \sqrt{v^{n} \pi^{n} |\Sigma|}} 
\Big[ 1 + \frac{1}{\nu} x^\top \Sigma^{-1} x  \Big]^{-(\nu + n)/2}.
$$

Compare this with the univariate version of the t density:

$$ \frac{\Gamma{(\nu +1)/2}}{\Gamma(\nu/2)\sqrt{\nu\pi}} \Big[ 1 + \frac{x^2}{2} \Big]^{-(\nu+1)/2}.$$

In both cases, $$\nu>2$$ is the degrees of freedom parameter.

A standard way to construct a random variable $$Z$$ with t-distribution is to use
a normal random variable $$X$$ and an independent chi-square random variable $$Y$$ and set

$$ Z = \frac{X}{\sqrt{Y/\nu}}.$$

This formula works for both the univariate and the multivariate case and can be
used to draw samples from the t distribution using independent samples of $$X$$ and
$$Y$$. Also, we get 

$$
\text{Cov} Z = \frac{\nu}{\nu-2} \text{Cov} X.
$$

This is because the univariate $$\chi^2$$ distribution with $$\nu$$ degrees of freedom is really 
a $$\text{Gamma}(\frac{\nu}{2}, \frac{1}{2})$$ distribution. The gamma densities are

$$ p_{\alpha,\beta}(x) = \frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x} 1_{[0, \infty)}(x), $$

with parameters $$\alpha>0$$ and $$\beta>0$$. Moreover, $$1/Y$$ is inverse-gamma distributed and thus 
$$\mathbb E \frac{1}{Y} = \frac{1}{\nu -2}.$$



### References

* Michael Roth. On the Multivariate t Distribution. [pdf](https://www.diva-portal.org/smash/get/diva2:618567/FULLTEXT02)
* Gregory Grundsen. [A Python Implementation of the Multivariate t-distribution.](https://gregorygundersen.com/blog/2020/01/20/multivariate-t/) (This code is now a part of sklearn)
* [Inverse-gamma distribution.](https://en.wikipedia.org/wiki/Inverse-gamma_distribution)
* Liu, Chuanhai, and Donald B. Rubin. "ML estimation of the t distribution using EM and its extensions, ECM and ECME." Statistica Sinica (1995): 19-39. [pdf](http://www3.stat.sinica.edu.tw/statistica/oldpdf/A5n12.pdf)
* Nadarajah, Saralees, and Samuel Kotz. "Estimation methods for the multivariate t distribution." Acta Applicandae Mathematicae 102, no. 1 (2008): 99-118. [pdf](http://www-users.math.umn.edu/~bemis/MFM/workshop/2011/estimating_multivariate_t.pdf)
* Martin Haugh. "The EM Algorithm." 2015. [pdf](http://www.columbia.edu/~mh2078/MachineLearningORFE/EM_Algorithm.pdf)

<!-- vim: set syntax=markdown: set spelllang=en_us: set spell: -->

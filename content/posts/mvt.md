---
title: "Studying the multivariate t-distribution (draft)"
date: 2020-10-08
modified: 2020-10-19
draft: true
markup: "markdown"
katex: true
tags:
    - machine-learning
    - probability-theory
---

# Definitions

Density of a (non-degenerate) multivariate normal distribution with zero mean is given by
\\[
f_X(x_1, \ldots, x_n) = \frac{1}{\sqrt{(2\pi)^n |\Sigma|}} 
\exp \Big( -\frac{1}{2} x^\top \Sigma^{-1} x \Big),
\\]
where \\(\Sigma\\) is a (positive-semidefinite) covariance matrix.

For comparison, the density of the multivariate t-distribution with zero mean is
\\[
\frac{\Gamma[(\nu + n)/2]}{\Gamma(\nu/2) \sqrt{v^{n} \pi^{n} |\Sigma|}}
\Big[ 1 + \frac{1}{\nu} x^\top \Sigma^{-1} x  \Big]^{-(\nu + n)/2}.
\\]

Compare this with the univariate version of the t density:
\\[
\frac{\Gamma{(\nu +1)/2}}{\Gamma(\nu/2)\sqrt{\nu\pi}} \Big[ 1 + \frac{x^2}{2} \Big]^{-(\nu+1)/2}
\\]

Gregory Grundsen
[provides](https://gregorygundersen.com/blog/2020/01/20/multivariate-t/) a
Python code to evaluate the multivariate t-density based on SciPy library.

A standard way to construct a random variable \\(Z\\) with t-distribution is to use
a normal random variable \\(X\\) and an independent chi-square random variable \\(Y\\) and set
\\[Z = \frac{X}{\sqrt{Y/n}}. \\]
This formula works for both the univariate and the multivariate case and can be
used to draw samples from the t distribution using samples from \\(X\\) and
\\(Y\\).

The density of the gamma distribution with parameters \\(a>0\\) and \\(\lambda>0\\) is
\\[
    p_{a,\lambda}(x) = \frac{\lambda^a}{\Gamma(a)}x^{a-1}e^{-\lambda x} 1_{\R_{\geq 0}}(x).
\\]
There is a nice formula for the n-th moment of the gamma distribution
\\[
    E X^n = \frac{a\cdot\ldots\cdot (n+a-1)}{\lambda^n}.
\\]

A univariate \\(\chi^2\\) distribution with \\(n\\) degrees of freedom is \\( \text{Gamma}(\frac{n}{2}, \frac{1}{2}). \\)

# Parameter Estimation

* The case when nu is known.

## Estimation via the EM Algorithm

* Derive the log-likelihood function using the density above.


# Standard Monte-Carlo study


# Closing remarks

* Observation: Since chi-square distribution is gamma, we could generalize the
  t distribution by varying the second parameter of gamma too.
* What is the Mahalanobis distance?

# References

Liu, Chuanhai, and Donald B. Rubin. "ML estimation of the t distribution using EM and its extensions, ECM and ECME." Statistica Sinica (1995): 19-39. http://www3.stat.sinica.edu.tw/statistica/oldpdf/A5n12.pdf 


* David Barber. Bayesian Reasoning and Machine Learning. http://www.cs.ucl.ac.uk/staff/d.barber/brml/

* Martin Haugh. "The EM Algorithm." 2015. http://www.columbia.edu/~mh2078/MachineLearningORFE/EM_Algorithm.pdf
* Nadarajah, Saralees, and Samuel Kotz. "Estimation methods for the multivariate t distribution." 
  Acta Applicandae Mathematicae 102, no. 1 (2008): 99-118.
  http://www-users.math.umn.edu/~bemis/MFM/workshop/2011/estimating_multivariate_t.pdf
* Michael Roth. On the Multivariate t Distribution. https://www.diva-portal.org/smash/get/diva2:618567/FULLTEXT02
* Gregory Grundsen. A Python Implementation of the Multivariate t-distribution. 
  https://gregorygundersen.com/blog/2020/01/20/multivariate-t/
* Dempster, A. P., N. M. Laird, and D. B. Rubin. "Maximum Likelihood from Incomplete Data via the EM Algorithm." Journal of the Royal Statistical Society. Series B (Methodological) 39, no. 1 (1977): 1-38. http://www.jstor.org/stable/2984875 https://www.ece.iastate.edu/~namrata/EE527_Spring08/Dempster77.pdf
* https://arxiv.org/pdf/1707.01130.pdf

<!-- vim: set syntax=markdown: set spelllang=en_us: set spell: -->

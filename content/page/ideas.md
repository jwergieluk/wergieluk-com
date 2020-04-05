---
title: "Article ideas"
date: 2020-04-05
draft: true
---


## Numerical Variance calculation

How to avoid implementing stuff like this:

    mean = self._metric_sums[key] / self._predictions_no[key]
    stdev = math.sqrt(max(self._metric_sums_of_squares[key] / self._predictions_no[key] - mean * mean, 0.0))

https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance





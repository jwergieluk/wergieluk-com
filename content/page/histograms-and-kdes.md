---
title: "A Meditation on Histograms and KDEs"
date: 2020-04-11
draft: false
katex: true
markup: "mmark"
slug: histograms-and-kdes
modified: 2020-04-13
---

#### Histograms and Kernel Density Estimators explained with Jenga bricks and sand piles

In this short blog post we are going to look at basic properties of 
histograms and kernel density estimators (KDEs) and show how they can be
useful to draw insights from the data. 

To illustrate the concepts, I will use a small data set I collected over 
last few months. Almost two yeast ago I started meditating regularly, and
at some point I added the daily meditation session duration to the list
of data I collect.   

{{< figure src="/histograms-and-kdes/meditation.png" >}}

As you can see, I usually meditate half an hour a day with some weekend 
outlier sessions that last for around an hour. But sometimes I am very tired
and I meditate for just 15 to 20 minutes. I end a session when I get a feeling
that it should end, so the session duration is a fairly random quantity.

The [meditation.csv](/histograms-and-kdes/meditation.csv) data set contains 
session duration in minutes.

I would like to know, how likely is it, for a randomly chosen session to last
between 25 and 35 minutes. And, how likely is it that a session lasts for 
50 minutes or more.

For that I can just sort the data points and plot the values.

{{< figure src="/histograms-and-kdes/x-axis.png" >}}

The problem with this visualization is that many values are very close and
plotted on top of each other: There is no way to tell how many 30 minute sessions
do I have in the data set. An idea, that leads to the construction of 
a histogram, is to use the vertical dimension of the plot distiguish between
regions with different data density. 

Let's divide the data range into intervals: 

    [10, 20), [20, 30), [30, 40), [40, 50), [50, 60), [60, 70)

For each data point in the first interval `[10, 20)` I put a rectangle
with area `1/129` (approx. `0.007`) and width 10 on the interval `[10, 20)`. 
It's like stacking Jenga bricks. Since we have 13 data points in the 
interval `[10, 20)` the stacked rectangles have the height of approx.
`0.01`:

{{< figure src="/histograms-and-kdes/histogram-construction-a.png" >}}

Let's repeate this for all the remaining intervals. 

{{< figure src="/histograms-and-kdes/histogram-construction-b.png" >}}

Since the total area of all the rectangles is one (we have `129` data points)
the upper boundary the stacked rectanges is a probability density function.
Densities are handy because they can be used to calculate probabilities.  For
example, the probability that a randomly chosen session will last between 25
and 35 minutes is the area between the density function (graph) and the x-axis
in the interval `[25, 35]`.

{{< figure src="/histograms-and-kdes/histogram-construction-c.png" >}}

This area equals `0.318`. Note that the height of the bars is only useful if
combined with the base width. In particular, we cannot read off probabilities
directly from the y-axis. 

Nevertheless, back-of-an-envelope calculations often yield satisfying results. 
For example, from the histogram plot we can infer that `[50, 60)` and 
`[60, 70)` bars have the height of around `0.005`. This means the probability
of a session duration between 50 and 70 minutes equals approximately
`20*0.005 = 0.1`. The exact calculation yields the probability of `0.1085`.

#### Choice of the interval subdivisions

The choice of the intervals (or 'bins') is arbitrary. We could also partition
the data range into intervals with length 1, or, use intervals with varying
length (this is uncommon). Using a small interval length makes the histogram
look more wiggly.

Histogram algorithm implementations in popular data science software packages
like `pandas` try to automatically produce histograms that are pleasant to the
eye by optimizing some score.

{{< figure src="/histograms-and-kdes/histogram-construction-d.png" >}}

#### Kernel Density Estimators

However we choose the subdivision interval length, a histogram will always look
more or less wiggly, because it is a stack of rectangles (think Jenga bricks).

Sometimes we are interested in calculating a smooth estimate of the density. For
that we can modify our method slightly. The histogram algorithm maps each data
point to a rectangle with a fixed area and places that rectangle "near" that
data point. What if instead using rectangles, we could put a "pile of sand"
on each data point and calculate how this sand stacks.

For example, the first observation in the data set equals `50.389`. Let's put
a nice pile of sand on it:

{{< figure src="/histograms-and-kdes/kde_a.png" >}}

Our model for a "pile of sand" is the following function which is called
the Epanechnikov kernel.

$$K(x) = \frac{3}{4}(1 - x^2),\text{ for } |x| < 1$$

The Epanechnikov kernel is a probability density function, which means, it is
positive or equal zero and the area under it's graph is equal to one. The function $$K$$ is
centered at zero but we can move it around by subtracting a constant from it's
argument $$x$$. 

{{< figure src="/histograms-and-kdes/epanechnikov_kernel_b.png" >}}

The above plot shows the graphs of 

$$x \mapsto K(x - 1) \text{ and } x\mapsto K(x - 2).$$

We can also tune the "stickiness" of the sand used. This can be done by scaling both
the argument and the value of the kernel function $$K$$ with a positive parameter $$h$$:

$$x \mapsto K_h(x) = \frac{1}{h}K\left(\frac{x}{h}\right).$$

The parameter $$h$$ is often called the _bandwidth_.

{{< figure src="/histograms-and-kdes/epanechnikov_kernel_c.png" >}}

The above plot shows the graphs of $$K_1$$, $$K_2$$, and $$K_3.$$ The function
$$K_h$$, for any $$h>0$$, is still a probability density -- we could show this
using some calculus. 

Let's generalize the histogram algorithm using the kernel function $$K_h$$. For
every data point $$x$$ in our data set containing `129` observations, we put a pile
of sand centered at that point $$x$$. In other words, given observations

$$x_1,...,x_{129},$$

we construct the function

$$f: x\mapsto \frac{1}{nh}K\left(\frac{x - x_1}{h}\right) +..+ \frac{1}{nh}K\left(\frac{x - x_{129}}{h}\right).$$

Note that each sand pile 

$$\frac{1}{nh}K\left(\frac{x - x_i}{h}\right),$$

has the mass of `1/129` -- just like the Jenga bricks used for the construction
of the histogram.  It follows that, the function $$f$$ is a probability
density function (the area under it's graph equals one). Let's have a look at it:

{{< figure src="/histograms-and-kdes/kde_b.png" >}}

Note that this graph looks similar to the histogram plots constructed earlier.

The function $$f$$ is called the *Kernel Density Estimator* (KDE). Estimator is
just a fancy word for a guess: We are trying guess density function $$f$$ that
describes well the randomness of the data.

The Epanechnikov kernel is just one possible choice of a sand pile model.
Another popular choice is the Gaussian bell curve (the density of the Standard
Normal distribution). In fact, every probability density function can be play
the role of a kernel to construct a kernel density estimator. The makes KDEs
very flexible. Let's use the following "box kernel",

{{< figure src="/histograms-and-kdes/box_kernel.png" >}}

to construct another KDEs for the meditation data.

{{< figure src="/histograms-and-kdes/kde_c.png" >}}

## Closing remarks

Recap the thing.



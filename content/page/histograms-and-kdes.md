---
title: "A Meditation on Histograms and KDEs"
date: 2020-04-11
draft: false
katex: true
markup: "mmark"
slug: histograms-and-kdes
modified: 2020-04-13
---

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

The problem with this visualization is that many values are repeated and
plotted on top of each other: There is no way to tell how many 30 minute sessions
do I have in the data set. An idea, that leads to the construction of 
a histogram, is to use the vertical dimension of the plot distiguish between
regions with different data density. 

Let's divide the data range into intervals: 

    [10, 20), [20, 30), [30, 40), [40, 50), [50, 60), [60, 70), 

For each data point in the first interval `[10, 20)` I put a rectangle
with area `1/129` (approx. `0.007`) and width 10 on the interval `[10, 20)`. 
It's like stacking Jenga bricks. Since we have 13 data point in the 
interval `[10, 20)` the stacked rectangles have the height of approx.
`0.01`:

{{< figure src="/histograms-and-kdes/histogram-construction-a.png" >}}

Let's repeate this for all the remaining intervals. 

{{< figure src="/histograms-and-kdes/histogram-construction-b.png" >}}

Since the total area of all the rectangles is one (we have `129` data points)
the upper boundary the stacked rectanges is a probability density function.
Densities are handy because they can be used to calculate probabilities. 
For example, the probability that a randomly chosen session will last between
25 and 35 minutes is, according to our histogram, the area between the
density and the x-axis in the interval `[25, 35]`




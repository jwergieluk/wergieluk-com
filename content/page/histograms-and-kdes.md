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
histograms and kernel density estimators (KDEs) and how they can be
useful to draw insights from the data. 

To illustrate the concepts, I will use small data set I collected over 
last few months. Almost two yeast ago I started meditating regularly, and
at some point I added the daily meditation session duration to the list
of data I collect.   

{{< figure src="/histograms-and-kdes/meditation.png" >}}

As you can see, I usually meditate for half an hour a day with some weekend 
outlier sessions that last for around an hour. But sometimes I am very tired
and I meditate for just 15 to 20 minutes. I end a session when I get a feeling
that it should end, so the session duration is a fairly random quantity.

The [meditation.csv](/histograms-and-kdes/meditation.csv) data set contains 
session duration in minutes.







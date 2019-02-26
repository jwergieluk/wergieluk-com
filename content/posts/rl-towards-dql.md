---
title: "Temporal-difference methods on steroids (draft)"
date: 2019-02-24
lastmod: 2019-02-24
draft: true
markup: "mmark"
tags:
    - machine-learning
    - reinforcement-learning
---

Deep Minds paper introducing the DQN: https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf

Riedmiller, Martin. "Neural fitted Q iteration–first experiences with a data efficient neural reinforcement learning method." European Conference on Machine Learning. Springer, Berlin, Heidelberg, 2005.


#### Experience replay 

* Helps to brake the correlations between consecutive SARS tuples. 
* Buffered experiences can be used multiple times. 


Prioritized Experience Replay
Tom Schaul, John Quan, Ioannis Antonoglou, David Silver https://arxiv.org/abs/1511.05952

Dueling Network Architectures for Deep Reinforcement Learning
Ziyu Wang, Tom Schaul, Matteo Hessel, Hado van Hasselt, Marc Lanctot, Nando de Freitas 
https://arxiv.org/abs/1511.06581


#### Fixed Q target.


#### DQN improvements


* Double-DQN: https://arxiv.org/abs/1509.06461 (2015) https://arxiv.org/abs/1509.06461
* https://www.ri.cmu.edu/pub_files/pub1/thrun_sebastian_1993_1/thrun_sebastian_1993_1.pdf


---
title: "Reinforcement learning notes (draft)"
date: 2019-02-24
draft: true
markup: "mmark"
---

# Videos

* Reinforcement Learning at Uni Waterloo https://www.youtube.com/playlist?list=PLdAoL1zKcqTXFJniO3Tqqn6xMBBL07EDc https://cs.uwaterloo.ca/~ppoupart/teaching/cs885-spring18/schedule.html
* Advanced Deep Learning and Reinforcement Learning course taught at UCL in partnership with Deepmind https://github.com/enggen/DeepMind-Advanced-Deep-Learning-and-Reinforcement-Learning
* Deep Reinforcement Learning (Berkeley) http://rail.eecs.berkeley.edu/deeprlcourse/ https://www.youtube.com/playlist?list=PLkFD6_40KJIxJMR-j5A1mkxK26gh_qg37
* Deep RL Bootcamp (Berkeley) https://sites.google.com/view/deep-rl-bootcamp/lectures
* YandexDataSchool Practical_RL https://yandexdataschool.com/edu-process/rl https://github.com/yandexdataschool/Practical_RL
* A Free course in Deep Reinforcement Learning from beginner to expert https://simoninithomas.github.io/Deep_reinforcement_learning_Course/

# Books

* D. Bertsekas. Reinforcement learning and optimal control. http://web.mit.edu/dimitrib/www/RLbook.html

# Papers

* Deep neural networks algorithms for stochastic control problems on finite horizon, Part 2: numerical applications
Achref Bachouch (UiO), Côme Huré (LPSM UMR 8001, UPD7), Nicolas Langrené (CSIRO), Huyen Pham (LPSM UMR 8001, UPD7) https://arxiv.org/abs/1812.05916

# Model implementations

* https://github.com/brendanator/atari-rl

# Hardware

* https://elinux.org/Jetson
* https://github.com/dusty-nv/jetson-reinforcement

# Models

## DQN 

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




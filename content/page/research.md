---
title: "Research"
date: 2019-02-24
draft: false
---

# Time Series
## Python software packages

* statsmodels
* https://github.com/TDAmeritrade/stumpy

https://www.quandl.com/data/LBMA/GOLD-Gold-Price-London-Fixing

## Literature

* McNeil, Alexander J., Rüdiger Frey, and Paul Embrechts. Quantitative risk management. Princeton university press, 2015.
* Hill, J. B. (2015). Robust estimation and inference for heavy tailed GARCH. Bernoulli, 21(3), 1629–1669. Retrieved from http://projecteuclid.org/euclid.bj/1432732032
* Bauwens, L. (2006). Multivariate GARCH models: a survey. Retrieved from http://onlinelibrary.wiley.com/doi/10.1002/jae.842/pdf
* Silvennoinen, A., & Teräsvirta, T. (2009). Multivariate GARCH models. Handbook of Financial Time Series. Retrieved from http://link.springer.com/chapter/10.1007/978-3-540-71297-8_9
* Aït-Sahalia, Y., & Kimmel, R. (2007). Maximum likelihood estimation of stochastic volatility models. Journal of Financial Economics, 83(2), 413–452. https://doi.org/10.1016/j.jfineco.2005.10.006

# Risk budgeting

* Choueifaty, Yves and Froidure, Tristan and Reynier, Julien, Properties of the Most Diversified Portfolio (July 6, 2011). Journal of Investment Strategies, Vol.2(2), Spring 2013, pp.49-70. . Available at SSRN: https://ssrn.com/abstract=1895459

# Shallow machine learning
## Gradient boosting software

Gradient Boosting Decision Trees = Decision trees + AdaBoost.

* LightGBM paper: https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree.pdf
* Xgboost: A scalable tree boosting system: https://dl.acm.org/ft_gateway.cfm?ftid=1775849&id=2939785
* CatBoost: gradient boosting with categorical features support. https://arxiv.org/pdf/1810.11363

* J. Friedman: Greedy function approximation: a gradient boosting machine: https://projecteuclid.org/download/pdf_1/euclid.aos/1013203451

# Deep learning
## Videos

* CS294-158 Deep Unsupervised Learning Spring 2019 https://sites.google.com/view/berkeley-cs294-158-sp19/home
* CS 294-112 at UC Berkeley: Deep Reinforcement Learning http://rail.eecs.berkeley.edu/deeprlcourse/ (Levine, 2018)
* https://sites.google.com/view/deep-rl-bootcamp/lectures (DRL Bootcamp Berkeley, 2017)
* http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html (Silver, 2015)
* CS234: Reinforcement Learning. Stanford University. Winter 2019. http://onlinehub.stanford.edu/cs234
* "Reinforcement Learning" course. University of Waterloo. Spring 2018. https://cs.uwaterloo.ca/~ppoupart/teaching/cs885-spring18/index.html

# Reinforcement learning

## Videos

* Reinforcement Learning at Uni Waterloo https://www.youtube.com/playlist?list=PLdAoL1zKcqTXFJniO3Tqqn6xMBBL07EDc https://cs.uwaterloo.ca/~ppoupart/teaching/cs885-spring18/schedule.html
* Advanced Deep Learning and Reinforcement Learning course taught at UCL in partnership with Deepmind https://github.com/enggen/DeepMind-Advanced-Deep-Learning-and-Reinforcement-Learning
* Deep Reinforcement Learning (Berkeley) http://rail.eecs.berkeley.edu/deeprlcourse/ https://www.youtube.com/playlist?list=PLkFD6_40KJIxJMR-j5A1mkxK26gh_qg37
* Deep RL Bootcamp (Berkeley) https://sites.google.com/view/deep-rl-bootcamp/lectures
* YandexDataSchool Practical_RL https://yandexdataschool.com/edu-process/rl https://github.com/yandexdataschool/Practical_RL
* A Free course in Deep Reinforcement Learning from beginner to expert https://simoninithomas.github.io/Deep_reinforcement_learning_Course/

## Books

* D. Bertsekas. Reinforcement learning and optimal control. http://web.mit.edu/dimitrib/www/RLbook.html

## Papers

* Deep neural networks algorithms for stochastic control problems on finite horizon, Part 2: numerical applications
Achref Bachouch (UiO), Côme Huré (LPSM UMR 8001, UPD7), Nicolas Langrené (CSIRO), Huyen Pham (LPSM UMR 8001, UPD7) https://arxiv.org/abs/1812.05916

## Model implementations

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

#### DQN improvements

* Double-DQN: https://arxiv.org/abs/1509.06461 (2015) https://arxiv.org/abs/1509.06461
* https://www.ri.cmu.edu/pub_files/pub1/thrun_sebastian_1993_1/thrun_sebastian_1993_1.pdf

## Policy gradients

Blog posts on policy gradient algorithms.

* https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html
* https://danieltakeshi.github.io/2017/03/28/going-deeper-into-reinforcement-learning-fundamentals-of-policy-gradients/
* https://medium.com/@jonathan_hui/rl-proximal-policy-optimization-ppo-explained-77f014ec3f12

### Literature

* https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf

# ASHRAE - Great Energy Prediction III

* Article cited in the problem description: https://www.mdpi.com/2504-4990/1/3/56
* https://www.kaggle.com/c/ashrae-energy-prediction/discussion/112958#latest-650382

# Kaggle
## IEEE-CIS Fraud Detection
### Winning solution

* Winning solution (Score 0.945884) write-up by Chris Deote
    * Part 1: https://www.kaggle.com/c/ieee-fraud-detection/discussion/111284

* "XGB Fraud with Magic scores LB 0.96" by Chris Deote: https://www.kaggle.com/cdeotte/xgb-fraud-with-magic-0-9600

* Konstantin Yakolev. Super-useful as it contains a general guidelines and tons of links. https://www.kaggle.com/c/ieee-fraud-detection/discussion/107697

### 2nd solution

* https://www.kaggle.com/c/ieee-fraud-detection/discussion/111321

### Others

* 17th place solution by Taemyung Heo

## Similar competitions and their writeups

* https://www.kaggle.com/c/ieee-fraud-detection/discussion/99987 (Link collection)




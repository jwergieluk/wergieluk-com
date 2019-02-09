---
title: "Markov Decision Processes"
date: 2019-02-08T21:09:51+01:00
draft: true
katex: true
markup: "mmark"
tags:
    - machine-learning
    - stochastic-processes
    - reinforcement-learning
---

Last week I began my journey of breaking into the field of reinforcement learning -- I 
started to watch first videos from the [Deep Reinforcement Learning 
Nanodegree](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893) program offered by Udacity. 

So far I had a very positive experience. The course sticks very closely to a
book, that seems to be the main monograph of the field, "Reinforcement
Learning" by R. Sutton and A. Barto. The book is available online and can be
downloaded for free from Richard Suttons homepage [^1]. I really like the fact
that the course and the book share (almost) the same notation. Also, many
examples discussed in the course are taken straight from the book. 

For me personally, the main limitation of the book is it's very verbose writing
style.  For example, Chapter 1 consisting of around 20 pages that can be
accurately summarized as follows: "Reinforcement learning is awesome". But it's
2019 and who haven't heard about computers playing Atari games, AlphaZero,
AlphaStar and so on. 

In this blog post I would like to summarize the notation and main results of
the theory of Markov decision processes (MDP) as outlined in the above book and
document my efforts implementing programs testing these results. 

# Notation and main results

Reinforcement learning tries to provide a mathematical framework and solution
methods for the problem of an agent/robot trying to achieve a goal in a given
environment.

$$\mathcal S^+$$ is the set of environment states, and $$\mathcal S$$ is the
set of environment states excluding the terminal (or "coffin", "game over")
state.  If the environment is at the $$s\in \mathcal S$$ the agent can decide
to take an action $$a\in\mathcal A(s)$$ which is the set of all admissible
actions at the state $$s$$ and is a subset of the set of all posible actions
$$\mathcal A$$.

The interactions between the agent and the environment are observed over a
discrete time index set $$\mathbb T = 0, 1, 2, \ldots$$. Thus we can define a
stochastic process 
$$S = (S_t)_{t\in\mathbb T}$$ taking
values in $$\mathcal S^+$$ and a process $$A = (A_t)_{t\in\mathbb T}$$ with
values in $$\mathcal A$$. Executing an action $$A_t$$ at the state $$S_t$$
yields a real-valued "reward" $$R_t$$. The agent's goal is to maximize the
expected cumulative reward $$\sum_{t\in\mathbb T} R_t$$ collected over the
lifetime.

We can protocol the agents interactions using the state-action-reward sequence as follows:

$$S_0, A_0, R_1, S_1, A_1, \ldots$$

This sequence is also called the _trajectory_. At $$t=0$$, the agent observes the 
environment state $$S_0$$ and decides to take the action $$A_0$$. This leads to a 
reward $$R_1$$ and a new state $$S_1$$ at $$t=1$$. 



# Supplementary literature

* Dititri Bertsekas, Reinforcement Learning and Optimal Control. http://web.mit.edu/dimitrib/www/RLbook.html Book draft, video lectures with slides.


[^1]: http://incompleteideas.net/book/the-book.html

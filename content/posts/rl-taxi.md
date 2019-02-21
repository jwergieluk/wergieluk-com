---
title: "Temporal-Difference learning and the taxi-v2 environment"
date: 2019-02-16
lastmod: 2019-02-20
draft: true
markup: "mmark"
tags:
    - machine-learning
    - reinforcement-learning
---

*Summary.* This documents my attempt at solving the taxi-v2 environment. To
benchmark the TD learning algorithms, I calculate the theoretical expected
episode reward for an optimal policy, generate an optimal policy, and show 
that there are an non-optimal policies that always generate optimal 
trajectories.

The description of the taxi-v2 environment can be found here: 

https://raw.githubusercontent.com/openai/gym/master/gym/envs/toy_text/taxi.py

There are 6 possible actions "south", "north", "east", "west", "pickup", and
"dropoff", labeled with integers 0 to 5.

The state is characterized by the following parameters:

    (taxi_row, taxi_col, passenger_location, destination) 

The taxi drives on a 5x5 matrix, there are 5 possible passenger locations (R,
G, Y, B, and Taxi), and 4 possible destinations:

    +---------+
    |R: | : :G|
    | : : : : |
    | : : : : |
    | | : | : |
    |Y| : |B: |
    +---------+

The state observations are encoded as Discrete(500) using the following encode() method: 

    def encode(self, taxi_row, taxi_col, pass_loc, dest_idx):
        # (5) 5, 5, 4
        i = taxi_row
        i *= 5
        i += taxi_col
        i *= 5
        i += pass_loc
        i *= 4
        i += dest_idx
        return i

Each action results in an reward of -1, except in the following two cases:
1. The "dropoff" action that ends the episode is rewarded with 20. (Not with -1 + 20 
as stated in the source code documentation)
2. Bogus "pickup" and "dropoff" actions get a reward of -10.

The initial state is chosen at random (uniformly) such that the passenger is 
not in the taxi, and pickup and dropoff positions are not equal.

Given this description, we can show that the expected end reward is *8.46333...*: 
In each episode, the
pickup and dropoff actions give us -1 + 20 reward points. To calculate the
expected travel path length, we can go over all possible initial states and
calculate shortest travel path for each. I've done this using the NetworkX[^1] 
package containing numerous graph algorithms.

    def expected_end_reward(self):
        expectation = -1.0 + 20.0
        path_lengths = 0.0
        path_no = 0.0
        for r0, c0, pickup_index, dropoff_index in itertools.product(
                range(5), range(5), range(4), range(4)):
            if pickup_index == dropoff_index:
                continue
            path_lengths += networkx.shortest_path_length(self.graph, (r0, c0), self.locs[pickup_index])
            path_lengths += networkx.shortest_path_length(self.graph, self.locs[pickup_index], self.locs[dropoff_index])
            path_no += 1.0
        expectation -= path_lengths/path_no
        return expectation

#### Score 

The leaderboard page in the gym wiki[^2] uses a running end reward average calculated
over 100 episodes which is a strange and unstable metric, since it is impacted significantly
by the randomness of the initial states. It makes much more sense to calculate 
the average reward over a large number of episodes (e.g. 25000) and compare that 
average with the theoretical expected reward calculated above. 

Also, we can look at the learned policy itself, and, for each state s determine 
whether the proposed action is optimal or not. 

#### Temporal-Difference learning

This task might look very straightforward at first, given the above interpretation and
our knowledge about taxis, but in fact the interaction with the environment from an agents 
perspective can appear quite puzzling. Here is an small part of a trajectory generated
by a random agent:

    action, reward, next_state
    2, -1, 393
    5, -10, 393
    2, -1, 393
    3, -1, 373
    4, -10, 373
    2, -1, 393

The class `Agent1` implements standard temporal-difference methods sarsa, sarsamax, and 
expected sarsa. 

Observations:

* Random initialization of the Q table seem to work better than using zero
or constant initialization. My guess is that random Q table yields a "noisy" 
initial policy that encourages exploratory behavior.

I ended up using expected sarsa with parameter values `alpha=0.05`, 
`gamma=0.9` (which has almost no noticable impact), and `epsilon=0.1` over the 
first 11000 episodes and `epsilon=0.0`
for the rest of the total number of 20000 episodes. 
The expected return of the policy estimated using this method matches the theoretical
optimal expected value of ~8.4 in most cases. Somehow surprisingly, the estimated
policy is not optimal and prescribes non-optimal actions for 8 states. It turns out that
this actually doesn't matter, because the states of the non-optimal state-action
pairs are never attained: 

    state 436: 4 1 T R  action 0: south
    state 437: 4 1 T G  action 0: south
    state 438: 4 1 T Y  action 0: south
    state 439: 4 1 T B  action 0: south
    state 456: 4 2 T R  action 5: dropoff
    state 457: 4 2 T G  action 2: east
    state 458: 4 2 T Y  action 0: south
    state 459: 4 2 T B  action 3: west
    state 498: 4 4 T Y  action 2: east

    +---------+
    |R: | : :G|
    | : : : : |
    | : : : : |
    | | : | : |
    |Y| : |B: |
    +---------+

In the above listing, the states are expanded to 4-tuples ("row", "column", "passenger
location", "dropoff location").

#### Visualization

I use a slightly modified version of the render() function to record the
episodes for this blog article. The destination is marked as red, the passenger
location with magenta, and a yellow taxi turns gray when it picks up the
passenger.


#### Implementation

https://gitlab.com/jwergieluk/rl/blob/master/rl01.py


# Similar write-ups and references

* https://cihansoylu.github.io/openai-taxi-v2-environment-q-learning.html
* https://blog.goodaudience.com/attempting-open-ais-taxi-v2-using-the-sarsa-max-algorithm-70a4de8c8c9c
* https://www.kaggle.com/angps95/intro-to-reinforcement-learning-with-openai-gym
* The original paper describing the taxi environment: https://arxiv.org/abs/cs/9905014

[^1]: https://networkx.github.io/documentation/stable/index.html
[^2]: https://github.com/openai/gym/wiki/Leaderboard#taxi-v2





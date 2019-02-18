---
title: "Temporal-Difference learning example taxi-v2 environment"
date: 2019-02-16T18:10:01+01:00
draft: true
markup: "mmark"
tags:
    - machine-learning
    - reinforcement-learning
---

The description of the taxi environment can be found here: 

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

The state observations are encoded as Discrete(500) using the encode() method: 

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

I use a slightly modified version of the render() function to record the
episodes for this blog article. The destination is marked as red, the passenger
location with magenta, and a yellow taxi turns gray when it picks up the
passenger.

This task might look very straightforward at first, given the above interpretation and
our knowledge about taxis, but in fact the interaction with the environment from an agents 
perspective can appear quite puzzling. Here is an small part of a trajectory generated
by a random agent:

| action | reward | next_state |
|--------|--------|------------|
| 2      | -1     | 393        |
| 5      | -10    | 393        |
| 2      | -1     | 393        |
| 3      | -1     | 373        |
| 4      | -10    | 373        |
| 2      | -1     | 393        |



{{< highlight py >}}
def sarsa(self, state, action, reward, next_state):
    """ Sarsa on-policy Q-table update rule """
    next_action = self.select_action(next_state)
    self.Q[state, action] = self.Q[state, action]*(1.0 - self.alpha) + self.alpha*(
            reward + self.gamma*self.Q[next_state, next_action])

def sarsamax(self, state, action, reward, next_state):
    """ Sarsamax aka Q-learning off-policy Q-table update rule """
    next_action = numpy.argmax(self.Q[next_state, :])
    self.Q[state, action] = self.Q[state, action]*(1.0 - self.alpha) + self.alpha*(
            reward + self.gamma*self.Q[next_state, next_action])

def expected_sarsa(self, state, action, reward, next_state):
    """ Expected Sarsa on-policy Q-table update rule """
    next_action = numpy.argmax(self.Q[next_state, :])
    policy_vector_for_next_state = numpy.repeat(self.epsilon()/self.dim_a, self.dim_a)
    policy_vector_for_next_state[next_action] += 1.0 - self.epsilon()
    self.Q[state, action] = self.Q[state, action] * (1.0 - self.alpha) + self.alpha * (
            reward + self.gamma * numpy.dot(policy_vector_for_next_state, self.Q[next_state, :]))
{{< / highlight >}}


https://gitlab.com/jwergieluk/rl/blob/master/rl01.py


# Similar attempts

* https://cihansoylu.github.io/openai-taxi-v2-environment-q-learning.html (best average 9.42)
* https://blog.goodaudience.com/attempting-open-ais-taxi-v2-using-the-sarsa-max-algorithm-70a4de8c8c9c(best average above 9)


https://www.kaggle.com/angps95/intro-to-reinforcement-learning-with-openai-gym


from enum import Enum
import numpy as np
from sys import maxint
import pandas as pd
from reward_calc import r,target,start,pr
from sample_data import dictionary

q = np.zeros_like(r)

"""class Agent:
  def __init__(self, eps=0.5, alpha=0.5, gamma=0.8):
    self.eps = eps # probability of choosing random action instead of greedy
    self.alpha = alpha # learning rate
    self.gamma = gamma
  def setStateAction(self, no_state_action):
    self.n_actions = no_state_action
    self.n_states = no_state_action
"""	
    
def update_q(index, state, next_state, action, alpha, gamma):
    #print('test3')	
    rsa = r[index][state, action]
    qsa = q[index][state, action]
    new_q = qsa + alpha * (rsa + gamma * max(q[index][next_state, :]) - qsa)
    q[index][state, action] = new_q
    # renormalize row to be between 0 and 1
    rn = q[index][state][q[index][state] > 0] / np.sum(q[index][state][q[index][state] > 0])
    q[index][state][q[index][state] > 0] = rn
    return r[index][state, action]

"""
def show_traverse():
    # show all the greedy traversals
    #for i in range(len(q)):
        current_state = start.id
        print(dictionary[current_state])
	print(pr[current_state])
        n_steps = 0
        while ((current_state != target[0].id)and(current_state != target[1].id)and(current_state != target[2].id)):
            next_state = np.random.choice([np.argmax(q[0][current_state]),np.argmax(q[1][current_state]),np.argmax(q[2][current_state])],p= pr[current_state])
	    current_state = next_state
            print(dictionary[current_state])
	    print(pr[current_state])		
            n_steps = n_steps + 1
        # cut off final arrow
        #traverse = traverse[:-3]
        #print("Greedy traversal for starting state %i" % (i+1))
        #print(traverse)
        #print("")
"""

# Core algorithm
gamma = 0.8
alpha = 0.5
n_episodes = 1e5
n_states = len(dictionary)
n_actions = len(dictionary)
epsilon = 0.5
random_state = np.random.RandomState(1999)
for index in range(len(target)):
	print('episode paths' + str(index))
	for e in range(int(n_episodes)):
	    states = list(range(n_states))
	    random_state.shuffle(states)
	    current_state = states[0]
	    traverse = str(e)+")"+"%i -> " % (current_state+1)
	    goal = False
	    while not goal:
		# epsilon greedy
		#print('test1')
		valid_moves = r[index][current_state] >= 0
		if random_state.rand() < epsilon:
		    actions = np.array(list(range(n_actions)))
		    actions = actions[valid_moves == True]
		    if type(actions) is int:
		        actions = [actions]
		    random_state.shuffle(actions)
		    action = actions[0]
		    next_state = action
		else:
		    if np.sum(q[index][current_state]) > 0:
		        action = np.argmax(q[index][current_state])
		    else:
		        # Don't allow invalid moves at the start
		        # Just take a random move
		        actions = np.array(list(range(n_actions)))
		        actions = actions[valid_moves == True]
		        random_state.shuffle(actions)
		        action = actions[0]
		    next_state = action
		#print('test2')
		reward = update_q(index, current_state, next_state, action, alpha=alpha, gamma=gamma)
		# Goal state has reward 100
		if reward > 90:
		    goal = True
		#print('test4')
		traverse += "%i -> " % (current_state+1)
		current_state = next_state
	    traverse = traverse[:-4]	
	    #print(traverse)	
"""print('q matrix')
for index, i in enumerate(q):
	print('q matrix' + str(index))
	for j in i:
		print(j)
"""
#show_traverse()
np.save('qmatrix.npy', q)

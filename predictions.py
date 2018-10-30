#from qlearningalgo import start,target
from reward_calc import start,target,pr
from sample_data import dictionary
import numpy as np

q = np.load('qmatrix.npy')
#print(q)
no_selected_target = np.zeros(len(target))
epsilon = 0.1

def probability(item):
	no_selected_target[item.clas] += 1
	p = []
	for i in len(target):
		p.append(no_selected_target[i]/np.sum(no_selected_target)) 
	return p

def show_traverse():
    # show all the greedy traversals
    #for i in range(len(q)):
        current_state = start.id
        print(dictionary[current_state])
	print(pr[current_state])
        n_steps = 0
       	while n_steps < 4:
        	if random_state.rand() < epsilon:		
       			next_state = np.random.choice([np.argmax(q[0][current_state]),np.argmax(q[1][current_state]),np.argmax(q[2][current_state])],p= probability(current_state))
			current_state = next_state
        		print(dictionary[current_state])
			n_steps = n_steps + 1
        # cut off final arrow
        #traverse = traverse[:-3]
        #print("Greedy traversal for starting state %i" % (i+1))
        #print(traverse)
        #print("")"""

show_traverse()

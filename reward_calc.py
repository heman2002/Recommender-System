import numpy as np
from sample_data import dictionary
from features import Model,Size,Brand,Cost,Picture,Sound

def round_of_nearest_half(number):
	return round(number * 2) / 2
start = dictionary[52]
distance = []
target = []
target.append(dictionary[43])
target.append(dictionary[7])
target.append(dictionary[1])

def distance_from_target1(item):
	temp = (((target[0].brand.value-item.brand.value)**2)+((target[0].size.value-item.size.value)**2)+((target[0].cost.value-item.cost.value)**2)+((target[0].picture.value-item.picture.value)**2)+((target[0].sound.value-item.sound.value)**2))
	return (round_of_nearest_half(temp**(1/2.0)))

def distance_from_target2(item):
	temp = (((target[1].brand.value-item.brand.value)**2)+((target[1].size.value-item.size.value)**2)+((target[1].cost.value-item.cost.value)**2)+((target[1].picture.value-item.picture.value)**2)+((target[1].sound.value-item.sound.value)**2))
	return (round_of_nearest_half(temp**(1/2.0)))

def distance_from_target3(item):
	temp = (((target[2].brand.value-item.brand.value)**2)+((target[2].size.value-item.size.value)**2)+((target[2].cost.value-item.cost.value)**2)+((target[2].picture.value-item.picture.value)**2)+((target[2].sound.value-item.sound.value)**2))
	return (round_of_nearest_half(temp**(1/2.0)))

distance.append(map(distance_from_target1, dictionary))
distance.append(map(distance_from_target2, dictionary))
distance.append(map(distance_from_target3, dictionary))
#print(distance)
distance = np.array(distance)
classes = np.argmin(distance, axis=0)
unique, counts = np.unique(classes, return_counts=True)
#print(counts)
#print(classes)
for index, item in enumerate(dictionary):
	#print(classes[index])
	item.assignClass(classes[index])

#print(dictionary)
	

#print('probability')
#for item in pr:
#	print(item)

#print(pr[1])
r = np.zeros((len(distance),len(dictionary),len(dictionary)))
for t, tar in enumerate(target):
	for item1 in dictionary:
		for item2 in dictionary:
			r[t][item1.id][item2.id] = distance[t][item1.id] - distance[t][item2.id]
			r[t][item2.id][item1.id] = distance[t][item2.id] - distance[t][item1.id]

for item in dictionary:
	if((distance[0][item.id]-distance[0][target[0].id])<=1):
		r[0][item.id][target[0].id] = 100
	if((distance[1][item.id]-distance[1][target[1].id])<=1):
		r[1][item.id][target[1].id] = 100
	if((distance[2][item.id]-distance[2][target[2].id])<=1):
		r[2][item.id][target[2].id] = 100
"""
for index, i in enumerate(r):
	print('reward matrix' + str(index))
	for j in i:
		print(j)"""

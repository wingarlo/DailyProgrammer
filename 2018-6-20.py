import math
from copy import deepcopy
'''
[2018-06-20] Challenge #364 [Intermediate] The Ducci Sequence
Logan Wingard
8/9/2018
'''

def ducciexe(thing):
	cpything = deepcopy(thing)
	for i in range(0,len(thing)):
		if (i == len(thing)-1):
			thing[i] = abs(cpything[i] - cpything[0])
		else: 
			thing[i] = abs(cpything[i] - cpything[i+1])
	return(thing)

def ducci(thing):
	count = 0
	while(sum(thing)):
		print(thing)
		thing = ducciexe(thing)
		count+=1
		if(count == 100):
			print("Repeating sequence.")
			break
	print(thing)
	print("Steps=")
	print(count)
while(1):
	thing = raw_input("List the integers separated by commas.")
	if(thing == "q" or thing == "quit"):
		break
	thing = tuple(thing.split(','))
	thing = map(int,thing)
	ducci(thing)

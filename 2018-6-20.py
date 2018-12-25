import math
from copy import deepcopy
'''
[2018-06-20] Challenge #364 [Intermediate] The Ducci Sequence
Logan Wingard
8/9/2018
'''

def ducciexe(thing):
	'''Perform Ducci subtraction step
	Input: tuple of ints
	Output: None
	Returns: Updated tuple
	'''
	cpything = deepcopy(thing)
	for i in range(0,len(thing)):									#Subtracts next value from current (or first if last value)
		if (i == len(thing)-1):
			thing[i] = abs(cpything[i] - cpything[0])
		else: 
			thing[i] = abs(cpything[i] - cpything[i+1])
	return(thing)

def ducci(thing):
	'''Perform Ducci calculation
	Input: tuple of ints
	Output: print statement of number of steps and values
	Returns: None
	'''
	count = 0
	prev = deepcopy(thing)
	prevprev = deepcopy(thing)
	while(sum(thing)):												#until the tuple is all zeros
		print(thing)
		prevprevprev = deepcopy(prevprev)
		prevprev = deepcopy(prev)
		prev = deepcopy(thing)										#Copy last 3 tuples
		thing = ducciexe(thing)										#perform subtraction
		count+=1													#inc counter
		if(thing == prev or thing == prevprev or thing == prevprevprev):#if Repeating Sequence detected
			print("Repeating sequence.")
			break
	print(thing)
	print("Steps=")
	print(count)													#output num steps

while(1):															#loops for quick manual testing
	thing = raw_input("List the integers separated by commas.")
	if(thing == "q" or thing == "quit"):							#user types "q" or "quit" to exit
		break
	thing = map(int,tuple(thing.split(',')))						#make input a tuple of ints
	prev = deepcopy(thing)
	prevprev = deepcopy(thing)
	prevprevprev = deepcopy(thing)									#make 3 copies for detecting repeating sequences
	ducci(thing)

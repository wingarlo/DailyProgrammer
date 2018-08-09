import math
'''
[2018-06-20] Challenge #364 [Intermediate] The Ducci Sequence
Logan Wingard
8/9/2018
'''


def ducci(thing):
    

while(1):
	thing = raw_input("List the integers separated by commas.")
	if(thing == "q" or thing == "quit"):
		break
	thing = tuple(thing.split(','))
	ducci(thing)

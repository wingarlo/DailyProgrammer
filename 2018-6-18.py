import random
import math
'''
[2018-06-18]Challenge #364 [Easy] Create a Dice Roller
Logan Wingard
8/9/2018
'''
random.seed()

def roll(com):
	nums = com.split("d")
	rolled = [0] * int(nums[0])
	for i in range(0,int(nums[0])):
		rolled[i] += random.randint(1,int(nums[1]))
	sumed = sum(rolled)
	return (rolled, sumed)
while(1):
	thing = raw_input()
	if(thing == "q" or thing == "quit"):
		break
	rolled, summed = roll(thing)
	print summed, ":", rolled
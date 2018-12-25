'''
[2018-12-17] Challenge #370 [Easy] UPC check digits
Logan Wingard
12/17/2018
'''

def addCheck(x):
	lst = 10 - ((((int(x[0]) + int(x[2]) + int(x[4]) + int(x[6]) + int(x[8]) + int(x[10]))*3) + (int(x[1]) + int(x[3]) + int(x[5]) + int(x[7]) + int(x[9]))) % 10)
	return(x + str(lst))
def check(x):
	if (len(x) != 12):
		return 0
	lst = 10 - ((((int(x[0]) + int(x[2]) + int(x[4]) + int(x[6]) + int(x[8]) + int(x[10]))*3) + (int(x[1]) + int(x[3]) + int(x[5]) + int(x[7]) + int(x[9]))) % 10)
	if (lst == 10):
		lst = 0
	if (lst == int(x[11])):
		return 1
	else:
		return 0

print( addCheck("03600029145"))



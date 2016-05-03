import math

def exp(x):
	return math.exp(x)



def printPoint():
	a = 2
	step = 100
	theta = 0
	counter = 0
	while counter < step:
		theta += 1/step
		r = a*theta
		print(math.cos(r), math.sin(r))
		counter+=1
printPoint()
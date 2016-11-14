import math
import random
import numpy as np

class State:
	x = 0
	y = 0
	solution = 0

	def  __init__(self,x,y,func):
		self.x = x
		self.y = y
		self.solution = func(x,y)

def ackley(x,y):
	return -20*math.exp(-0.2*math.sqrt(0.5*(x**2 + y**2)))-math.exp(0.5*(math.cos(2*3.1415*x) + math.cos(2*3.1415*y)))+math.exp(1)+20

def annealing(func):
	f = open('ann_out.txt','w')
	f.write(',Simulated Annealing')
	f.write("\n")

	currentState = State(random.randint(-32,32),random.randint(-32,32),func)
	T = 1
	while T > 0.001:
		T-=0.0001
		candidateState = State(random.randint(-32,32),random.randint(-32,32),func)
		diffE = currentState.solution - candidateState.solution
		if diffE > 0:
			currentState = candidateState
		else:
			if math.exp(diffE/T) >= random.uniform(0,1):
				currentState = candidateState

		f.write(str(T))
		f.write(',')
		f.write(str(currentState.solution))
		f.write("\n")

	return currentState

globalMinimumState = annealing(ackley)

print('x ='+str(globalMinimumState.x)+', y = '+str(globalMinimumState.y)+ ', solution = '+str(globalMinimumState.solution))
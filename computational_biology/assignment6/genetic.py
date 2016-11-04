import math
import random
import numpy as np
import copy

def ackley(x,y):
	return -20*math.exp(-0.2*math.sqrt(0.5*(x**2 + y**2)))-math.exp(0.5*(math.cos(2*3.1415*x) + math.cos(2*3.1415*y)))+math.exp(1)+20

class State:
	x = 0
	y = 0
	solution = 0

	def  __init__(self,x,y,func):
		self.x = x
		self.y = y
		self.solution = func(x,y)
		self.f = func

	def update(self,x,y):
		self.x = x
		self.y = y
		self.solution = self.f(x,y)

def genetic(func):
	p = []

	# generate initial population
	for i in range(0,100):
		p.append(State(random.randint(-32,32),random.randint(-32,32),func))

	pNew = []

	for a in range(0,100):
		# evolve next generation
		for i in range(0,50):
			# find individual with best fitness
			b = p[0]
			for j in range(0,len(p)):
				if p[j].solution < b.solution:
					b = p[j]

			biggest = copy.deepcopy(b)
			p.remove(b)

			# find individual with second best fitness
			b = p[0]
			for j in range(0,len(p)):
				if p[j].solution < b.solution:
					b = p[j]

			biggest2 = copy.deepcopy(b)
			p.remove(b)

			# crossover
			pNew.append(State(biggest.x,biggest2.y,func))
			pNew.append(State(biggest.y,biggest2.x,func))

		# mutate and evaluate
		for i in range(0,10):
			idx = i*random.randint(1,5)
			pNew[idx].update(pNew[idx].x,random.randint(-32,32))
		for i in range(0,10):
			idx = i*random.randint(1,5)
			pNew[idx].update(random.randint(-32,32),pNew[idx].y)

		p = pNew

	b = p[0]
	for j in range(0,len(p)):
		if p[j].solution < b.solution:
			b = p[j]

	biggest = copy.deepcopy(b)
	return biggest

globalMinimumState = genetic(ackley)

print('x ='+str(globalMinimumState.x)+', y = '+str(globalMinimumState.y)+ ', solution = '+str(globalMinimumState.solution))
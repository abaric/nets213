import random
import math

# Code to generate 90 random numbers split by line

for i in range(0, 90):
	x1 = random.random()
	y1 = math.floor(x1)
	x2 = random.random()
	y2 = math.floor(x2)
	x3 = random.random()
	y3 = math.floor(x3)
	while (y1 == y2 || y2 == y3):
		x1 = random.random()
		y1 = math.floor(x1)
		x2 = random.random()
		y2 = math.floor(x2)
		x3 = random.random()
		y3 = math.floor(x3)
	
	print y1
	print y2
	print y3
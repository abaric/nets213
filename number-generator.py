import random
import math

# Code to generate 90 random numbers split by line

for i in range(0, 90):
	x1 = random.random() * 1000
	y1 = math.floor(x1)
	x2 = random.random() * 1000
	y2 = math.floor(x2)
	# x3 = random.random() * 1000
	# y3 = math.floor(x3)
	while (y1 == y2):
		x1 = random.random()
		y1 = math.floor(x1)
		x2 = random.random()
		y2 = math.floor(x2)
	
	print '%d%s%d' %(y1,", ",y2)

for i in range(0, 90):
	x1 = random.random() * 1000
	y1 = math.floor(x1)
	x2 = random.random() * 1000
	y2 = math.floor(x2)
	x3 = random.random() * 1000
	y3 = math.floor(x3)
	while (y1 == y2) | (y2 == y3) | (y1 == y3):
		x1 = random.random()
		y1 = math.floor(x1)
		x2 = random.random()
		y2 = math.floor(x2)
		x3 = random.random()
		y3 = math.floor(x3)

	print '%d%s%d%s%d' %(y1,", ",y2,", ", y3)


for i in range(0, 90):
	x1 = random.random() * 1000
	y1 = math.floor(x1)
	x2 = random.random() * 1000
	y2 = math.floor(x2)
	x3 = random.random() * 1000
	y3 = math.floor(x3)
	x4 = random.random() * 1000
	y4 = math.floor(x4)
	while (y1 == y2) | (y2 == y3) | (y1 == y3) | (y1 == y4) | (y2 == y4) | (y3 == y4):
		x1 = random.random()
		y1 = math.floor(x1)
		x2 = random.random()
		y2 = math.floor(x2)
		x3 = random.random()
		y3 = math.floor(x3)
	
	print '%d%s%d%s%d%s%d' %(y1,", ",y2,", ", y3, ", ", y4)

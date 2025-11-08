"""
1 2 5 10
4 3 6 11
9 8 7 12
16 15 14 13
"""
import math

n = 45
mapSize = int(math.sqrt(n))+1
x,y=0,0
d=[[0 for __ in range(mapSize)] for _ in range(mapSize)]

boxSize = 0
for i in range(n):
	d[y][x]=i+1
	if x == 0 and y == boxSize:
		boxSize += 1
		x=boxSize
		y=0
	elif y < boxSize:
		y += 1
	elif y == boxSize:
		x -= 1

for k in range(mapSize):
	print('\t'.join(map(str,d[k])))


import math

bx = 1
by = 1
px = 2
py = 2

d = math.sqrt((bx - px)**2 + (by - py)**2)
a = math.acos((px - bx) / d) 

print(d, a)
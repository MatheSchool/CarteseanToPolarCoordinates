import math

bx = 0
by = 0
px = 18.09987
py = 26.98775

d = math.sqrt((bx - px)**2 + (by - py)**2)
a = math.acos((px - bx) / d) 

print(d, a)
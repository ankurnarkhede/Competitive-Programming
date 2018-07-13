
import sys
import math


r=6400

p1=0
q1=-1

p2=0
q2=179

x1=r*math.cos(math.radians(p1))*math.cos(math.radians(q1))

y1=r*math.cos(math.radians(p1))*math.sin(math.radians(q1))

z1=r*math.sin(p1)

x2=r*math.cos(math.radians(p2))*math.cos(math.radians(q2))

y2=r*math.cos(math.radians(p2))*math.sin(math.radians(q2))

z2=r*math.sin(p2)

dist=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)+math.pow(z2-z1,2))

print(dist)



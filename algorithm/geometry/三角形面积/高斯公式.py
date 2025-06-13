
def area(x1,y1,x2,y2,x3,y3):
    return abs((x2-x1)* (y3-y1) -(x3-x1)*(y2-y1))/2

def area2(x1,y1,x2,y2,x3,y3):
    return abs((x1*y2 + x2*y3+ x3*y1) - (x2*y1+x3*y2+x1*y3))/2

x1  = 0
y1 =0
x2= 6
y2 =0 
x3 =0
y3 =6

print(area(x1,y1,x2,y2,x3,y3))
print(area2(x1,y1,x2,y2,x3,y3))

for x3 in range(40):
    for y3 in range(40):
        if area(x1,y1,x2,y2,x3,y3) !=area2(x1,y1,x2,y2,x3,y3):
            print(x3,y3)

import math
def area3(a,b,c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def tranArea(x1,y1,x2,y2,x3,y3):
    a,b,c = distance(x1,y1,x2,y2),distance(x2,y2,x3,y3),distance(x1,y1,x3,y3)
    return area3(a,b,c)

for x3 in range(40):
    for y3 in range(40):
        if abs(area(x1,y1,x2,y2,x3,y3) -tranArea(x1,y1,x2,y2,x3,y3)) >= 0.1**10:
            print(x3,y3, area(x1,y1,x2,y2,x3,y3),tranArea(x1,y1,x2,y2,x3,y3))
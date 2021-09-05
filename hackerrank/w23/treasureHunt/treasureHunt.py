
filename = "input/input11.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


a,b = map(float , ins[0].strip().split())

c,d = map(float , ins[1].strip().split())
e,f = -d,c
x= float((a *c + b * d) /(c**2 +d **2))
y= float((b*c -a*d) /(c**2 +d**2))

print x 
print y
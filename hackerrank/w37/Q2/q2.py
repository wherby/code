filename = "input/input00.txt"
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


def add(x,y):
    return x+y

q, = map(int , ins[0].strip().split())
index=1
x =0
for i in range(q):
    ls=ins[index+i].strip().split()
    if ls[0]=="add":
        x1 = add(x,int(ls[1]))
    else:
        x1 = int(ls[1])
    if x1 >x:
        x = x1
print x
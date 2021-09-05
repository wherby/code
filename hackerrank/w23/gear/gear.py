#https://www.hackerrank.com/contests/w23/challenges/gears-of-war
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


q, = map(int , ins[0].strip().split())
index =1


for i in range(q):
	n,=map(int , ins[index+i].strip().split())
	if n%2==0:
		print "Yes"
	else:
		print "No"

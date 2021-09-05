#https://www.hackerrank.com/challenges/string-reduction
#http://stackoverflow.com/questions/8033553/stumped-on-a-java-interview-need-some-hints/8715230
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

def getCountABC(ls):
	ca=len(filter(lambda x: x=='a',ls))
	cb=len(filter(lambda x: x=='b',ls))
	cc=len(filter(lambda x: x=='c',ls))
	if ca == len(ls) or cb==len(ls) or cc==len(ls):
		return len(ls)
	if ca%2 == cb%2 and ca%2 == cc%2:
		return 2
	else:
		return 1


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	st= ins[index+i].strip()
	print getCountABC(st)
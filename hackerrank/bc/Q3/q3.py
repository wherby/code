filename = "input/input02.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import bisect

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

n,m = map(int , ins[0].strip().split())
al =map(int , ins[1].strip().split())

tnum=0
ttnum =0
dic1 = {}
sl= []
for i in range(m):
	t = al[i]
	if t not in dic1:
		dic1[t] =[1]
	else:
		dic1[t].append(i)
	bisect.insort(sl,t)
	it = sl.index(t)
	tnum = tnum + i -it - len(dic1[t]) +1
ttnum = tnum
#print ttnum
#print n -m
for i in range(n-m):
	t1 = al[i]
	t = al[i +m]
	it1 = sl.index(t1)
	tnum = tnum - it1 
	sl.remove(t1)
	#print sl
	dic1[t1] =dic1[t1][1:]
	if t not in dic1:
		dic1[t] =[1]
	else:
		dic1[t].append(m+i)
	bisect.insort(sl,t)
	it = sl.index(t)
	tnum = tnum + m -it - len(dic1[t]) 
	#print tnum,sl
	ttnum = ttnum +tnum

print ttnum





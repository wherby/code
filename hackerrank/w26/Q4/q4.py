filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/contests/w26/challenges/street-parade-1


import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


#print ins

def findStart(m,ls):
	global mi,ma,q
	index = 0
	lstIdex=index
	rem = m 
	mi1 = mi 
	ma1 = ma
	mi2 = mi
	ma2 = ma
	###HINT: consider the edge case
	if m < ma:
		return ls[0]- m

	while rem > ma1 + ma2 and lstIdex + 1 < q:
		#print rem, index,lstIdex
		t = ls[lstIdex +1] -ls[lstIdex]
		if t >= mi and t <=ma:
			#print rem
			#print t,q ,lstIdex, ma1,ma2,ma
			rem = rem - t
			if index == lstIdex  and index != 0:
				if ls[index] - ls[index -1] >=ma:
					ma1 = ma
				elif ls[index] - ls[index -1] <mi:
					ma1=0
				else:
					ma1 = ls[index] - ls[index -1]
			lstIdex = lstIdex +1
			
			if lstIdex + 1 >=q:
				ma2 = ma
			else:
				ma2 = ls[lstIdex +1] - ls[lstIdex]
				if ma2 >=  ma:
					ma2=ma
		if t < mi:
			index = lstIdex+1
			lstIdex = index
			rem = m
		if t > ma:
			index = lstIdex +1
			lstIdex = index
			rem = m
			ma1 = ma
		if lstIdex +1 == q:
			ma2= ma
	for i in range(mi,ma1 +1):
		if (rem - i >=  mi and rem -i <= ma2) or (rem - i ==0):
			#print ls[index:index+10]
			return ls[index] -i 
		



q, = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())
m,mi,ma = map(int , ins[2].strip().split())
re = findStart(m,ls)
print re




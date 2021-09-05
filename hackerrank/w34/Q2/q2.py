filename = "input/input28.txt"
f=open(filename,'r')

#https://www.hackerrank.com/contests/w34/challenges/maximum-gcd-and-sum/submissions/code/1302383325
###*****Good******
##http://codeforces.com/blog/entry/9923
##You are wrong. Not all implementations of "sieve of Eratosthenes" require N Log Log N time. 
##Algorithm above is N log N because N + N/2 + N/3 + N/4 ... + N/N = O(N log N)

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


maxgcd = 1
sumgcd =1
q, = map(int , ins[0].strip().split())
index=1
als= map(int , ins[1].strip().split())
bls= map(int, ins[2].strip().split())

alsMax= max(als)
blsMax =max(bls)
ablsMin = min(alsMax,blsMax)
ablsMax = max(alsMax,blsMax)
alsTree =[]
blsTree =[]
adir = {}
bdir = {}

for i in als:
	adir[i] =1
for i in bls:
	bdir[i] =1

for i in range(ablsMin+1):
	alsTree.append([])
	blsTree.append([])

for i in range(ablsMin,0,-1):
	for j in range(1,ablsMax/i +1):
		t = i*j
		if t in adir:
			alsTree[i].append(t)
		if t in bdir:
			blsTree[i].append(t)
	if len(alsTree[i])> 0 and len(blsTree[i])>0:
		re = max(alsTree[i]) + max(blsTree[i])
		print re
		break
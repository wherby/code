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


#print ins

def geneRn(rn,r0,g,seed,p):
	n = len(rn)
	rn[0] =r0
	for i in range(1,n):
		rp = rn[i-1]
		rn[i] = (rp *g +seed) %p

def search(stack,t,cnt):
	global ls, rn,left,right,n
	stack2 =[]
	for s1 in stack:
		k = rn[s1%n]
		if k > n/2:
			ls[t+n] =1 
			return ([],t,cnt+1)
		start = k * -1
		end = k+1
		if left> s1 +start:
			for s2 in range(s1+start,left+1):
				#print s1+start,left
				tp = (s1 + s2 ) %n 
				if ls[tp] == 0:
					stack2.append(tp)
					ls[tp] = 1
			left =s1+start
		if right< s1+end:	
			for s2 in range(right, s1+end): 
				tp = (s1 + s2 ) %n 
				if ls[tp] == 0:
					stack2.append(tp)
					ls[tp] = 1
			right =s1+end-1
	#print ls,left,right
	return (stack2,t,cnt +1)



def searchD(stack,t,cnt):
	global ls, rn
	if ls[t ] !=0:
		return cnt
	if len(stack) ==0:
		return -1
	#print ls
	while len(stack)!=0 and ls[t]==0:
		stack,t,cnt= search(stack,t,cnt)
		#print ls
	#print ls,ls[t],t
	if ls[t ] !=0:
		return cnt
	if len(stack) ==0:
		return -1




n,s,t = map(int , ins[0].strip().split())


left = s 
right =s 
n3 = n *3
r0,g,seed,p= map(int , ins[1].strip().split())
rn=[0] *n
geneRn(rn,r0,g,seed,p)
#print rn
ls = [0]*n
ls[s] =2
stack=[s]
re = searchD(stack,t,0)
print re
#print r0,g,seed,p
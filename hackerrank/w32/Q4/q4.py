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


#$print ins

def factorize(n):
	'''Adapted from http://www.math.utah.edu/~carlson/notes/python.pdf'''
	if n < 2:
		return []
	d = 2
	factors = []
	while not n % d:
		factors.append(d)
		n /= d
	d = 3
	while n > 1 and d * d <= n:
		if not n % d:
			factors.append(d)
			n /= d
		else:
			d += 2
	if n > 1:
		factors.append(n)
	return factors

def geneFact(factors,xxx):
	n =len(factors)
	factors=factors*2
	if n == 0:
		return 
	re={}
	for i in range(1,2**(n*2)):
		t1 = i
		tp=1
		index=0
		while t1!=0:
			if t1 %2==1:
				tp = tp *factors[index]
			t1 = t1 /2
			index = index +1
		re[tp] =1
	# for k,v in re.items():
	# 	r2= xxx *xxx /k
	# 	if xxx == 6:
	# 		print "***********"
	# 	re[r2] =1
	#print re,i
	#print xxx
	return re

factLS=[0] * 10001
for i in range(1000):
	fals = factorize(i)
	fcls2 = geneFact(fals,i)
	#print fcls2,i,fals
	factLS[i] = fcls2
#print factLS



n, = map(int , ins[0].strip().split())

ls= ins[1].strip()
als={}
bls={}
cls={}
for i in range(n):
	if ls[i] == 'a':
		als[i+1] =1
	if ls[i] =='b':
		bls[i+1] =1
	if ls[i] == 'c':
		cls[i+1] =1
cnt = 0
for key,value in bls.items():
	k2 = key * key
	tp = factLS[key]
	#print tp,key
	for k2,v2 in tp.items():
		if k2 in als:
			k3 = key * key /k2
			if k3 in cls:
				cnt = cnt +1
				#print k2,k3
#print als,bls,cls
print cnt
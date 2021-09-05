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
	dic1={}
	for x in factors:
		if x in dic1:
			dic1[x] = dic1[x] +1
		else:
			dic1[x] =1
	n = len(dic1)
	sls=[]
	for k,v in dic1.items():
		n1 = v *2 +1
		t1=[]
		for i in range(n1):
			t1.append(k**i)
		sls.append(t1)
	#print sls
	re=[]
	ini=[1]
	for i in range(n):
		ini2=[]
		t1 = sls[i]
		for k in ini:
			tls1 = map(lambda x: k* x, t1)
			tls1 = filter(lambda x: x <=500000,tls1)
			ini2.extend(tls1)
		ini = ini2
	#print ini
	return ini





n, = map(int , ins[0].strip().split())


factLS=[0] * (n+1)
for i in range(n):
	fals = factorize(i)
	fcls2 = geneFact(fals,i)
	#print fcls2,i,fals
	factLS[i] = fcls2
#print factLS

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
	tp = factLS[key]
	#print tp,key
	for k2 in tp:
		if k2 in als:
			k3 = key * key /k2
			if k3 in cls:
				cnt = cnt +1
				#print k2,k3
#print als,bls,cls
print cnt
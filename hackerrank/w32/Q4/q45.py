filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import datetime

if  "f" in locals():
	inputA=f
else:
	inputA=sys.stdin


ins=[]
for line in inputA:
	ins.append(line)

PList= [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,
211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,
307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,
401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,
503,509,521,523,541,547,557,563,569,571,577,587,593,599,
601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,
701,709,719,727,733,739,743,751,757,761,769,773,787,797,
809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,
907,911,919,929,937,941,947,953,967,971,977,983,991,997]
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

def factorizeUsingPList(n):
	global PList,fls
	'''Adapted from http://www.math.utah.edu/~carlson/notes/python.pdf'''
	if n < 2:
		return ([n],1)
	d = 2
	factors = []
	# while not n % d:
	# 	factors.append(d)
	# 	n /= d
	# d = 3
	index = 0
	d = PList[index]

	while n > 1 and d * d <= n:
		if not n % d:
			factors.append(d)
			if len(fls[n/d]) ==0:
				tls,xxxx1= factorizeUsingPList(n/d)
				fls[n/d] =tls
			factors.extend(fls[n/d])
			return (factors,d)
		else:
			index = index +1
			d =PList[index]
	if n > 1:
		factors.append(n)
	return (factors,1)


def geneFact(factors,i,xx):
	global factLS
	if xx != 1 and len(factLS[i/xx]) !=0:
		ini = factLS[i/xx]
		ini2= []
		t1 = [xx**0,xx**1,xx**2]
		dic1={}
		re=[]


		for k in t1:
			for x in ini:
				tp = x *k
				if tp < 500000:
					if tp not in dic1:
						dic1[tp] =1
						re.append(tp)

		return re#re#list(set(re))
	else:
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

def getFact(x):
	fals,xx = factorizeUsingPList(x)
	#print fals
	#fls[i] = fals
	if xx == 1 :
		return []
	else:
		fcls2 = geneFact(fals,i,xx)
		return fcls2



n, = map(int , ins[0].strip().split())
#print datetime.datetime.now()

factLS=[]
fls=[] 
for i in range(500001):
	factLS.append([])
	fls.append([])

#print factLS
def getFact(x):
	fals,xx = factorizeUsingPList(x)
	#print fals
	#fls[i] = fals
	if xx == 1 :
		return []
	else:
		fcls2 = geneFact(fals,i,xx)
		return fcls2
#print datetime.datetime.now()
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

blst=bls.keys()

for i in blst:
	fals,xx = factorizeUsingPList(i)
	#print fals
	fls[i] = fals
	fcls2 = geneFact(fals,i,xx)
	#print fcls2,i,fals
	factLS[i] = fcls2


for key,value in bls.items():
	tp = factLS[key]
	#print tp,key
	for k2 in tp:
		if k2 in als:
			k3 = key * key /k2
			if k3 < 500000:
				if k3 in cls:
					cnt = cnt +1
				#print k2,k3
#print als,bls,cls
print cnt
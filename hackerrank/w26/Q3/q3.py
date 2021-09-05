filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w26/challenges/twins

import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


def isPrimeT(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True



primeList = range(2,32000)
primeList = filter(isPrimeT,primeList)



ls=[]
def getCand(m,n):
	global ls
	start = m / 6 +1
	if start ==0:
		start = 1
	end = (n-1) / 6 +1
	for i in range(start,end):
		ls.append(i*6 -1)

def isPrime(n):
	global primeList
	sn = math.sqrt(n)
	for i in primeList:
		if i > sn:
			break
		if n%i==0:
			return False
	return True

def isPrimePair(n):
	if isPrime(n) and isPrime(n+2):
		return True
	else:
		return False



m,n = map(int , ins[0].strip().split())
getCand(m,n)

ls = filter(isPrimePair,ls)

cont = len(ls)
if m <=3 and n >=5:
	cont = cont +1
print cont

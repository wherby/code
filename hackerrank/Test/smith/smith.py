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

n, = map(int , ins[0].strip().split())


pl=[]
def getPrimes(n):
	isPrime =True
	for i in range(2,int(math.sqrt(1+n))+1):
		if n%i ==0 :
			pl.append(i)
			n=n/i
			isPrime = False
			getPrimes(n) 
			break
	if isPrime == True:
		if n != 1:
			pl.append(n)
		return

def getN(n):
	nl=[]
	while n !=0:
		t1= n%10
		n=n/10
		nl.append(t1)
	s2=sum(nl)
	return s2

getPrimes(n)
s=sum(map(getN,pl))


s2=getN(n)

if s==s2:
	print 1
else:
	print 0
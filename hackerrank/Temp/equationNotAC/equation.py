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


def gcd(a, b):
 if a < b:
  a, b = b, a
 while b != 0:
  temp = a % b
  a = b
  b = temp
 return a

def findMin(re):
	minD=1000000000
	minP=0
	for i in range(len(re)):
		t1,t2=re[i]
		tc=math.sqrt(t1**2 +t2**2)
		if tc < minD:
			minP=(t1,t2)
			minD=tc 
	return minP


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	a,b,c,= map(int , ins[index+i].strip().split())
	zzz=c/(a*b)
	c=c-a*zzz
	f=1
	d=gcd(a,b)
	f=gcd(d,c)
	a,b,c = a/f,b/f,c/f
	d = c / b
	e=gcd(a,b)
	z=d 
	re=[]
	ss=min(0,d-a/e)
	while z>ss:
		if (c-b*z) %a ==0:
			if (c-b*z)/a !=0:
				re.append(((c-b*z)/a,z))

				break
		z=z-1
	x,y=re[0]
	x,y= x+zzz*b,y-zzz*a

	print str(x)+" "+str(y)
	
		
		

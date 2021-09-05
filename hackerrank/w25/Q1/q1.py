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

<<<<<<< HEAD

print ins



q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index+i].strip().split())
=======
#LIB :GCD LCM, Factor
def gcd(a, b):
 if a < b:
  a, b = b, a
 while b != 0:
  temp = a % b
  a = b
  b = temp
 return a

def lcm(m,n):
 return m * n / gcd(m,n)



m,n=map(int , ins[0].strip().split())
al= map(int , ins[1].strip().split())
bl= map(int , ins[2].strip().split())
a1=al[0]

for i in range(1,m):
	a1=lcm(a1,al[i])
b1=bl[0]
for i in range(1,n):
	b1=gcd(b1,bl[i])
re=[]
c1 = b1/a1
d1= int(math.sqrt(c1))
for i in range(1,d1+1):
	if c1%i ==0:
		re.append(i)
		if i != c1/i:
			re.append(c1/i)
print len(re)
>>>>>>> 8d796735e4b8fcc464f22c31cb7f2a5792066ed5

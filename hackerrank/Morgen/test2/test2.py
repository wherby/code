filename = "input/input15.txt"
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
    ins.append(line.strip())
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
		pl.append(n)
		return

getPrimes(n)
dic={}
for i in range(len(pl)):
	t1=pl[i]
	if t1 in dic:
		dic[t1]=dic[t1]+1
	else:
		dic[t1]=1
ks=dic.keys()

rs=[]
def times(a,b,n1):
	for i in range(n1):
		a=a*b
	return a

def getNum(dic,numI,ks,i,start):
	i= i % (len(ks))
	global n,rs
	n1=ks[i]
	n2=dic[n1]
	if numI < n:
		rs.append(numI)
	else:
		return
	if start == i:
		return
	for j in range(n2*2+1):
		#print "xx"  + str(j) +"cc" +str(n1)
		#print times(numI,n1,j)
		getNum(dic,times(numI,n1,j),ks,i+1 ,start)

for i in range(len(ks)):
	t1=ks[i]
	t2=dic[t1]
	for j in range(1,t2+1):
		nt=times(1,t1,t2+j)
		#print nt
		#print "XXX"
		getNum(dic,nt,ks, i+1,i)
print len(set(rs))
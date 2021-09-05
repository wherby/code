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

def geneLs():
	global ls,n,k,p,m
	for i  in range(n-1):
		ls[n-2-i] = p * ls[n-1-i] %m

def getKey():
	global ls,k,lsindex,sotls
	lsindex = sorted(range(len(ls)), key=lambda k: ls[k])
	sotls = sorted(ls)


def incIndex():
	global ls, lsindex,k,gvalue,sotls,m,mls
	index = 0
	while mls[index] == k-1:
		mls[index] = 0
		index = index +1
	gvalue = gvalue + sotls[index] 
	mls[index] = mls[index] +1
	for i in range(index):
		gvalue = (gvalue - sotls[i] *(k-1))
	return gvalue%m
	



def inc():
	global ls, lsindex,k,dic1,gvalue,n,m,mls,f1ls,f2ls
	index = 0
	k1=-1
	k1 =incIndex()
	while k1 not in dic1:
		dic1[k1] =1
		k1 =incIndex()
	f1ls=list(mls)
	keyFind = k1
	mls = [0]*n
	gvalue =0
	k2 =0
	while k2 != keyFind :
		k2 = incIndex()
	f2ls = list(mls)



gvalue=0

n,k,p,m = map(int , ins[0].strip().split())
ls = [1]*n
lsindex=[]
sotls =[]
mls=[0] *n
f1ls= []
f2ls=[]
geneLs()
getKey()
dic1={}

inc()
def generateLS():
	global lsindex, ls, f1ls,f2ls,n
	ls1 = [1]*n
	ls2 =[1]*n
	for i in range(n):
		t = f1ls[i]
		ls1[lsindex[i]] = ls1[lsindex[i]] + t
		t2 = f2ls[i]
		ls2[lsindex[i]] = ls2[lsindex[i]] + t2
	ls1 = map(str,ls1)
	ls2 = map(str,ls2)
	print " ".join(ls1)
	print " ".join(ls2)

#print lsindex,f1ls,f2ls
generateLS()



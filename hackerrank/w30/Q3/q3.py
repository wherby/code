

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

#https://www.hackerrank.com/contests/w30/challenges/melodious-password


n = 1


vl=['a','e','i','o','u']
cl=map(chr, range(ord('a'), ord('z')+1))
for a in  vl:
    cl.remove(a)
cl.remove('y')
def getN(ls1,ls2,n):
    global vl,cl
    nls1=[]
    nls2=[]
    if n == 0:
        ls1.extend(ls2)
        #print ls1
        return ls1
    for x1 in cl:
        for x2 in ls1:
            tp = x2+x1
            nls2.append(tp)
    for x1 in vl:
        for x2 in ls2:
            tp = x2 +x1
            nls1.append(tp)
    return getN(nls1,nls2,n-1)

re = getN([""],[""],n)
for i in re:
	print i
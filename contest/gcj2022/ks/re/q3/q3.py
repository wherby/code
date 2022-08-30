# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba82c5
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


# Will timeout

def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res
def getAllComb(n,pls):
    ret =[]
    for p in pls:
        while n%p ==0:
            ret.append(p)
            n = n//p 
    return ret

def verify(k,n,ls):
    isGood =True
    for i in range(0,n,k):
        if ls[:k]!= ls[i:i+k]:
            isGood = False
            break
    return isGood

def resolve():
    m, = tuple(list(map(lambda x: int(x),input().split())))
    ls2  = input()
    plsm = get_prime(m)
    allC = getAllComb(m,plsm)
    ret =ls2
    for i in range(2<<len(allC)):
        acc =1
        for j in range(len(allC)):
            if (1<<j) &i :
                acc *= allC[j]
        if verify(acc,m,ls2) and len(ret)> acc:
            ret = ls2[:acc]
    return ret

    
    
def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)
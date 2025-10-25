
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/final_product_chapter_2_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


FILEDEBUG=True

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./out.txt', 'w')
    sys.stdout = f

import math
def getPrime(M):
    is_prime = [1]*(M+1)
    prs =[]
    for i in range(2,M+1):
        if is_prime[i]:
            prs.append(i)
            for j in range(2*i,M+1,i):
                is_prime[j] = 0 
    return prs
prs = getPrime(10**7 +10)
def getAllDiv(n):
    vals = {}
    for p in prs:
        if p*p > n:
            break
        if n%p == 0:
            vals[p] = 0 
            while n%p ==0:
                vals[p] +=1
                n=n // p 
    if n >1:
        vals[n] =1
    factors =[1]
    for x in vals:
        c = vals[x]
        k = len(factors)
        for i in range(c*k):
            factors.append(factors[i]*x)
    return factors
mod = 10**9+7

def resolve():

    N,A,B = list(map(lambda x: int(x),input().split()))
    divs = getAllDiv(B)
    def waysToFill(k):
        res =1 
        i = 2
        while i*i <=k:
            if k%i ==0:
                e = 0
                while k % i == 0:
                    e += 1  # 统计有多少个质因子 i
                    k //= i
                res = res * math.comb(e + N - 1,e)%mod
            i += 1
        if k >1:
            res = res*N %mod 
        return res
    acc = 0
    for d in divs:
        if d <=min(A,B):
            acc += waysToFill(d) *waysToFill(B//d)%mod 
        #print(d,acc,A,B,waysToFill(A),waysToFill(B//A) ,B//A)
    return acc%mod

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))


for i in range(int(input())):
    op(i)
#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/tower_rush_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



mod = 10**9+7

from collections import Counter
def prepare(M):
    # 初始化数组
    mu = [1] * M  # 莫比乌斯函数
    F = [0] * M   # 最小质因子
    q = []        # 存储质数
    
    mu[1] = 1     # 规定mu[1] = 1
    
    for i in range(2, M):
        if not F[i]:  # i是质数
            F[i] = i
            q.append(i)
            mu[i] = -1  # 质数的mu值为-1
        
        # 用当前已筛出的质数q[j]去标记合数i*q[j]
        for p in q:
            if i * p >= M:
                break
            F[i * p] = p  # 合数i*p的最小质因子是p
            if i % p == 0:
                mu[i * p] = 0  # i*p包含平方因子p^2
                break
            else:
                mu[i * p] = -mu[i]  # 根据mu的定义更新
    
    return mu, F, q

import math
def getMlengthGcd(ls,m,queries):
    c = Counter(ls)
    mx = max(ls)
    mu, F, primes = prepare(mx+1)
    gcd_count = [0]*(mx+1)
    for i in range(1,mx+1):
        for j in range(i*2,mx+1,i):
            c[i] += c[j]
    #print(c)
    # print(mx)
    # print(queries,len(gcd_count))
    for i in queries:
        if i > mx:
            continue
        gcd_count[i] += math.comb(c[i],m)%mod
        for j in range(2,mx//i +1):
            gcd_count[i] += mu[j]*math.comb(c[j*i],m)%mod
    return gcd_count

def getAllDiv(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    def getAllComb(pls,n):
        ret =[]
        for p in pls:
            while n%p ==0:
                ret.append(p)
                n = n//p 
        return ret
    allC = getAllComb(res,n)
    ret =set([])
    for i in range(2<<len(allC)):
        acc =1
        for j in range(len(allC)):
            if (1<<j) &i :
                acc *= allC[j]
        ret.add(acc)
    return ret

def resolve():
    N,K,D = list(map(lambda x: int(x),input().split()))
    ls = list(map(lambda x: int(x),input().split()))
    cnt = 0 
    allD = getAllDiv(D)
    allD = list(allD)
    a1 = 1 
    for i in range(1,K+1):
        a1 = a1*i%mod
    cnt = sum(getMlengthGcd(ls,K,allD))* a1 %mod
    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)
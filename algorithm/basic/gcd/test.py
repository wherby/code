# 求 0<x<y<MX  0<=x<y<Mx 条件下 x*y%k ==0 的组合数量
from math import gcd
from collections import defaultdict,deque
MX = 2000
kk =2*3*5*2*3

def f1():
    cnt = 0
    for i in range(1,MX):
        for j in range(1,i):
            if i*j %kk==0:
                cnt +=1
    return cnt 

def f2():
    divisors = [[] for _ in range(MX)]
    for i in range(1,MX):
        for j in range(i,MX,i):
            divisors[j].append(i)
    cnt =0
    c = defaultdict(int)
    for i in range(1,MX):
        k2 = kk //gcd(i,kk)
        cnt += c[k2]
        for d in divisors[i]:
            c[d] +=1
    return cnt 
print(f1())
print(f2())


# 从零开始
def f3():
    cnt = 0
    for i in range(MX):
        for j in range(i):
            if i*j %kk==0:
                cnt +=1
    return cnt 

def f4():
    divisors = [[] for _ in range(MX)]
    for i in range(1,MX):
        for j in range(i,MX,i):
            divisors[j].append(i)
    cnt =0
    c = defaultdict(int)
    for i in range(1,MX):
        cnt +=1  # x 为 0 时候，一定符合
        k2 = kk //gcd(i,kk)
        cnt += c[k2]
        for d in divisors[i]:
            c[d] +=1
    return cnt 
print(f3())
print(f4())
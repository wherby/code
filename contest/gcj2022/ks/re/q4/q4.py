#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
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

import math
import itertools

visit ={}
g =[]
s =set()

def func(op,num,res):
    if op =="+":
        return res +int(num)
    if op =="-":
        return res - int(num)
    if op == "*":
        return res *int(num)
    if op == "/":
        return math.floor(res / int(num))
        
def resolve():
    N,P,M,Ar,Ac = tuple(list(map(lambda x: int(x),input().split())))
    dir =[]
    for _ in range(4):
        fun,nm = tuple(list(input().split()))
        dir.append((fun,nm))
    mx= 0
    dp= [[[-10**10]*(N+1) for _ in range(N+1)] for _ in range(M+1)]
    st = [(Ar,Ac,M,0)]
    while st:
        ar,ac,m,val = st.pop()
        if m ==0 :
            continue
        if ar >1:
            op,num = dir[0]
            ar1,ac1,m1,val1 = ar-1,ac,m-1,func(op,num,val)
            if val1 > dp[m1][ar1][ac1]:
                dp[m1][ar1][ac1] = val1
                mx = max(mx,val1)
                st.append((ar1,ac1,m1,val1))
        if ac<N:
            op,num = dir[1]
            ar1,ac1,m1,val1 = ar,ac+1,m-1,func(op,num,val)
            if val1 > dp[m1][ar1][ac1]:
                dp[m1][ar1][ac1] = val1
                mx = max(mx,val1)
                st.append((ar1,ac1,m1,val1))
        if ac >1:
            op,num = dir[2]
            ar1,ac1,m1,val1 = ar,ac-1,m-1,func(op,num,val)
            if val1 > dp[m1][ar1][ac1]:
                dp[m1][ar1][ac1] = val1
                mx = max(mx,val1)
                st.append((ar1,ac1,m1,val1))
        if ar<N:
            op,num = dir[3]
            ar1,ac1,m1,val1 = ar+1,ac,m-1,func(op,num,val)
            if val1 > dp[m1][ar1][ac1]:
                dp[m1][ar1][ac1] = val1
                mx = max(mx,val1)
                st.append((ar1,ac1,m1,val1))
    return str(mx)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)
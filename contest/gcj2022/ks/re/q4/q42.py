# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba86e6#problem
# TLE
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
from collections import defaultdict

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
    localDic ={} 
    for i in range(P):
        x,y,c =tuple(list(map(lambda x: int(x),input().split())))
        localDic[(x,y)] =(i,c)
    mx= -1
    dp= defaultdict(lambda:-10*10)
    dp[(Ar,Ac,M,0)] =0
    st = [(Ar,Ac,M,0,0)]
    while st:
        #print(st)
        ar,ac,m,val,status = st.pop()
        if (ar,ac) in localDic:
            i,cost = localDic[(ar,ac)]
            if (1<<i)&status ==0 and dp[(ar,ac,m,status|(1<<i))] < val +cost:
                dp[(ar,ac,m,status|(1<<i))]= val +cost
                st.append((ar,ac,m,val+cost, status |(1<<i)))
        if status ==(1<<P )-1:
            mx = max(mx,val)            
        if m ==0 :
            continue
        if ar >1:
            op,num = dir[0]
            ar1,ac1,m1,val1 = ar-1,ac,m-1,func(op,num,val)
            if val1 > dp[(ar1,ac1,m1,status)]:
                dp[(ar1,ac1,m1,status)] = val1
                st.append((ar1,ac1,m1,val1,status))
        if ac<N:
            op,num = dir[1]
            ar1,ac1,m1,val1 = ar,ac+1,m-1,func(op,num,val)
            if val1 > dp[(ar1,ac1,m1,status)]:
                dp[(ar1,ac1,m1,status)] = val1
                st.append((ar1,ac1,m1,val1,status))
        if ac >1:
            op,num = dir[2]
            ar1,ac1,m1,val1 = ar,ac-1,m-1,func(op,num,val)
            if val1 > dp[(ar1,ac1,m1,status)]:
                dp[(ar1,ac1,m1,status)] = val1
                st.append((ar1,ac1,m1,val1,status))
        if ar<N:
            op,num = dir[3]
            ar1,ac1,m1,val1 = ar+1,ac,m-1,func(op,num,val)
            if val1 > dp[(ar1,ac1,m1,status)]:
                dp[(ar1,ac1,m1,status)] = val1
                st.append((ar1,ac1,m1,val1,status))
    return str(mx) if mx !=-1 else "IMPOSSIBLE"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)
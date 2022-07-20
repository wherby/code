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

            
def verify(comb):
    global visit,s,g
    s = set(comb)
    visit ={}
    st =comb
    while st:
        a = st.pop()
        s.add(a)
        if a not in visit:
            visit[a] =1
            for b in g[a]:
                if b not in visit:
                    st.append(b)
                    visit[b] =1
    #print(comb,s)
    return len(s) 
        
def resolve():
    global g
    n,m,k = tuple(list(map(lambda x: int(x),input().split())))
    ls =[]
    g=[[] for _ in range(n+1)]
    for i in range(m):
        a,b =  tuple(list(map(lambda x: int(x),input().split())))
        g[b].append(a)
    cand = [i for i in range(1,n+1)]
    cnt =0
    for i in range(1,n+1):
        if verify([i]) > k:
            cnt +=1
    return str(cnt)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)
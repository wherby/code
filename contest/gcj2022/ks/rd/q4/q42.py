#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/ts1_input.txt"
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

acc =0

def dfs(x):
    global g,visit,acc
    visit[x]=1
    acc +=1
    #print(acc)
    for a in g[x]:
        if a not in visit:
            if acc  >20:
                break
            dfs(a)
            
    return acc
    
def verify(i,k):
    global visit,s,g
    cnt = dfs(i)   
    #print(comb,s)
    #print(cnt)
    return cnt >k 
        
def resolve():
    global g,visit,acc
    n,m,k = tuple(list(map(lambda x: int(x),input().split())))
    ls =[]
    g=[[] for _ in range(n+1)]
    for i in range(m):
        a,b =  tuple(list(map(lambda x: int(x),input().split())))
        g[b].append(a)
    cand = [i for i in range(1,n+1)]
    cnt =0
    for i in range(1,n+1):
        visit={}
        acc =0
        if verify(i,k):
            cnt +=1
    return str(cnt)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)
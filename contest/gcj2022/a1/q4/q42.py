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

def dfs(i,g,dp,ls,dp1,visit):
    visit[i] =1
    if len(g[i]) ==0:
        dp[i] =0
    else:
        mn = ls[i]
        mx = ls[i]
        for a in g[i]:
            dfs(a,g,dp,ls,dp1,visit)
            mn = min(mn,dp1[a])
            mx = max(mx,dp1[a])
        dp[i] = mn
        dp1[i] = mx
    

def resolve():
    inp = int(input())
    ls = [0]+list(map(lambda x: int(x),input().split()))
    ls2 = list(map(lambda x: int(x),input().split()))
    g =[[] for _ in range(inp+1)]
    for i in range(inp):
        if i+1 >ls2[i]:
            g[ls2[i]].append(i+1)
        else:
            g[0].append(i+1)
    #print(g)
    sm = sum(ls)
    dp= [0]*(inp+1)
    dp1 = [0]*(inp+1)
    for i in range(inp):
        dp[i+1] =ls[i+1]
        dp1[i+1]= ls[i+1]
    #print(dp,dp1)
    visit=[0]*(inp+1)
    for i in range(inp+1):
        if visit[i]==0:
            dfs(i,g,dp,ls,dp1,visit)
    #print(dp,dp1)
    return sm -sum(dp)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)
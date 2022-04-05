# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
# dfs using stack
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

sm =0



def dfs(i,g,dp,ls):
    global sm
    n = len(g)
    visited=[0]*n
    st =[i]
    sq = []
    while st:
        a = st.pop()
        sq.append(a)
        if visited[a]:
            continue
        visited[a] =1
        for x in g[a]:
            st.append(x)
    for a in sq[::-1]:
        if len(g[a]) ==0:
            continue
        else:
            t1 = []
            for x1 in g[a]:
                t1.append(dp[x1])
            t1.sort()
            dp[a] = max(t1[0],dp[a])
            sm += sum(t1) - t1[0]
    sm +=dp[0]
    return sm

    # if len(g[i]) ==0:
    #     return
    # else:
    #     mn = ls[i]
    #     t1 = []
    #     for a in g[i]:
    #         dfs(a,g,dp,ls)
    #         mn = min(mn,dp[a])
    #         t1.append(dp[a])
    #     t1.sort()
    #     dp[i] = max(t1[0],dp[i])
    #     sm += sum(t1)- t1[0]
    #     #print(sm,i,t1,dp)
    #     if i ==0:
    #         sm += dp[i]
    

def resolve():
    global sm
    inp = int(input())
    ls = [0]+list(map(lambda x: int(x),input().split()))
    ls2 = list(map(lambda x: int(x),input().split()))
    g =[[] for _ in range(inp+1)]
    
    for i in range(inp):
        if i+1 >ls2[i]:
            g[ls2[i]].append(i+1)
        else:
            g[0].append(i+1)
    #print(g,ls2)
    sm = 0
    dp= [0]*(inp+1)
    for i in range(inp):
        dp[i+1] =ls[i+1]
    #print(dp,dp1)
    dfs(0,g,dp,ls)
    #print(dp)
    return sm

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)
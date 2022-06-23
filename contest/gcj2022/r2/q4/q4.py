#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
from cmath import inf
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/ts1_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


from math import inf
def work(ls,C):
    ls.sort()
    n = len(ls)
    dp = [inf]*(n+1)
    sa,sb = [0]*(n+1),[0]*(n+1)
    for i,a in enumerate(ls):
        sa[i+1] = sa[i]
        sb[i+1] = sb[i]
        if ls[i][1] ==0:
            sa[i+1] += ls[i][0]
        else:
            sb[i+1] += ls[i][0]
    dp[0] = 0
    last ={}
    last[0]=0
    delta =0
    for i in range(1,n+1):
        delta += 1 if ls[i-1][1] == 0 else -1
        if i == 1:
            dp[i] = ls[i-1][0]
        else:
            dp[i] = min(dp[i-1] + ls[i-1][0], dp[i-2] +ls[i-1][0]+ C * (ls[i-1][1] == ls[i-2][1]) )
        #print(delta,sa,sb,dp)
        if delta in last:
            j = last[delta]
            if ls[j][1] ==0:
                dp[i] = min(dp[i], dp[j] +sb[i]-sb[j])
            else:
                dp[i] = min(dp[i], dp[j] + sa[i] -sa[j])
        #print(dp,last)
        last[delta] =i
    return dp[n]
        

def resolve():
    N,C = tuple(list(map(lambda x: int(x),input().split())))
    a,b =[],[]
    for i in range(N):
        x,s = tuple(list(map(lambda x: int(x),input().split())))
        if x >0:
            a.append([x*2,s])
        else:
            b.append([-x*2,s])
    re = work(a,C)+work(b,C)
    return re

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)
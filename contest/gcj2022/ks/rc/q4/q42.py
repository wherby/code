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

mod = 10**9+7
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret
def inv(x):
    return quickPow(x,mod-2)
N= 402
fact =[1]*N
invFact = [1]*N
for i in range(2,N):
    fact[i] = fact[i-1]*i %mod
for i in range(1,N):
    invFact = inv(fact[i])


def resolve():
    n = int(input())
    str1= input()
    dp = [[[0]*N for _ in range(N)] for _ in range(N)]
    for i in range(n):
        dp[i+1][i][0]=1
        dp[i][i+1][1]=1
    for le in range(2,n+1):
        for l in range(n-le+1):
            r = l+le
            for plen in range(1,le):
                dp[l][r][plen] =dp[l][r-1][plen] +dp[l+1][r][plen] - dp[l+1][r+1][plen]
            if str1[l] == str1[r-1]:
                dp[l][r][2]+=1
                for plen in range(3,le+1):
                    dp[l][r][plen] += dp[l+1][r-1][plen-2]
     
    
    return sm -sum(dp)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)
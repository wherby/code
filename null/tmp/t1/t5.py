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


# https://atcoder.jp/contests/arc192/editorial/12201

MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
ans = 1
for i in range(2, max(A) + 1):
    a = [0] * (N - 1)
    for j in range(N - 1):
        while A[j] % i == 0:
            a[j] += 1
            A[j] //= i
    sa = sum(a)
    if sa == 0:
        continue
    pows = [1] * (sa + 1)
    for j in range(1, sa + 1):
        pows[j] = (pows[j - 1] * i) % MOD
    dp = [[pows[j], 0] for j in range(sa + 1)]
    dp[0] = [0, 1]
    print(A,a)
    print("dp: ",i, dp)
    for j in range(N - 1):
        ndp = [[0, 0] for _ in range(sa + 1)]
        for k in range(sa + 1):
            if k - a[j] >= 0:
                nxt = 0
                if k - a[j] == 0:
                    nxt = 1
                ndp[k - a[j]][nxt] += dp[k][0] * pows[k - a[j]]
                ndp[k - a[j]][nxt] %= MOD
                ndp[k - a[j]][1] += dp[k][1] * pows[k - a[j]]
                ndp[k - a[j]][1] %= MOD
            if a[j] != 0 and k + a[j] <= sa:
                ndp[k + a[j]][0] += dp[k][0] * pows[k + a[j]]
                ndp[k + a[j]][0] %= MOD
                ndp[k + a[j]][1] += dp[k][1] * pows[k + a[j]]
                ndp[k + a[j]][1] %= MOD
        dp = ndp
        #print(j,dp)
    nsum = 0
    for j in range(sa + 1):
        nsum = (nsum + dp[j][1]) % MOD
    print("IIII",i,dp)
    ans = (ans * nsum) % MOD
print(ans)
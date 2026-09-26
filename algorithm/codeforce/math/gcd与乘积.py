# https://codeforces.com/gym/104544/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0819/solution/cf104544a.md
# 题目求的是对一个已知的数字x的数字乘积整除的最小子数组长度
# 对一个已知的数字的因子，每个数字的贡献度是gcd(x,a)，这样贡献的因子种类就被压缩了
# 然后是构成x的状压DP， 对于一个因子来说，如果不能对现有DP改善，则这个因子就不会有作用
# 计算当前因子是否对当前状态有作用，使用当前状态的补集和因子求GCD。



import init_setting
from cflibs import *
def main():
    n, x = MII()
    
    factors = []
    
    for i in range(1, 100000):
        if x // i < i: break
        if x % i == 0:
            factors.append(i)
            if x // i != i:
                factors.append(x // i)
    
    factors.sort()
    
    k = len(factors)
    d = {v: i for i, v in enumerate(factors)}
    
    cnt = [0] * k
    
    for v in MII():
        cnt[d[math.gcd(v, x)]] += 1
    
    gcds = [[0] * k for _ in range(k)]
    
    for i in range(k):
        for j in range(k):
            gcds[i][j] = math.gcd(factors[i], factors[j])
    
    dp = [inf] * k
    dp[0] = 0
    
    for i in range(k):
        for _ in range(cnt[i]):
            ndp = dp[:]
            flg = False
            
            for j in range(k):
                nj = d[factors[j] * gcds[d[x // factors[j]]][i]]
                if ndp[nj] > dp[j] + 1:
                    ndp[nj] = dp[j] + 1
                    flg = True
            
            if not flg:
                break
            
            dp = ndp
    
    print(dp[-1] if dp[-1] < inf else -1)
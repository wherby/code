# https://codeforces.com/gym/105500/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0418/solution/cf105500j.md
# 假设k个数字和为N，然后求所有不同的组合中每位数字的平方和 之和
# 
# algorithm/codeforce/docs/Ferrers 图（Young Diagram）的转置（Conjugate）性质/Ferrers 图（Young Diagram）的转置（Conjugate）性质.md
# algorithm/codeforce/docs/Ferrers 图（Young Diagram）的转置（Conjugate）性质/为什么不用乘y.md
# algorithm/codeforce/docs/Ferrers 图（Young Diagram）的转置（Conjugate）性质/外层循环中的i的意义.md

# i 表示当前DP dp[m]: 保存的是已知 i 个元素和为 m 的情况， 
# 为什么 只求了i 的时候，就可以计算ans?  因为 y = k - i  表示剩余的元素都是相等的某个值的时候的贡献
# 为什么在y个值是x的时候，计算贡献的时候不用乘y? algorithm/codeforce/docs/Ferrers 图（Young Diagram）的转置（Conjugate）性质/为什么不用乘y.md
# 简单来说就是利用了每次计算至少有多少个x 的时候就平均累加了y次， 如果有 y次，则至少有 1，2。。y 次 的时候DP 里就会计算一次


import init_setting
from cflibs import *
def main():
    n, k = MII()
    mod = 10 ** 9 + 7
    
    ans = 0
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(k):
        ndp = [0] * (n + 1)
        
        for j in range(n + 1):
            if i and i + j <= n:
                dp[i + j] += dp[j]
                dp[i + j] %= mod
            if i + 1 <= n and j + 1 <= n:
                ndp[j + 1] += dp[j]
                ndp[j + 1] %= mod
        
        y = k - i
        for x in range(1, n // y + 1):
            ans += x * x * dp[n - y * x] % mod
            ans %= mod
        
        dp = ndp
    
    print(ans)
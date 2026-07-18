# https://codeforces.com/gym/103306/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0715/solution/cf103306a.md
# 因为节点数目有限，所以可以用枚举所有的状态mask来得到状态转移，dp[i][mask] 表示 mask 有 i个联通区域
# 而 dp[1][mask]状态递推的关键变量，但是dp[1][mask]是可以由容斥原理求取，因为mask对应的边数量级很大，所以只能通过mask里边的所有组合数量去除 mask里所有点的组合中大于1的联通区域的数量得到这个dp[1][mask] 
# 转移逻辑的不重不漏，为什么包含最高位的mask放置在单独部分dp[1][mask]反而能不重不漏？ algorithm/codeforce/dp/docs/DP子状态转移推导.md
# 遍历所有子状态的情况下实现了子状态递推


import init_setting
from lib.cflibs import *
def main():
    n, m = MII()
    
    mod = 998244353
    cnt = [1] * (1 << n)
    
    for _ in range(m):
        u, v = GMI()
        
        for i in range(1 << n):
            if i >> u & 1 and i >> v & 1:
                cnt[i] = cnt[i] * 2 % mod
    
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    
    for i in range(1, 1 << n):
        bit = 1 << i.bit_length() - 1
        cur = i
        
        while cur >= bit:
            for j in range(2, n + 1):
                dp[j][i] += dp[1][cur] * dp[j - 1][i - cur] % mod
                dp[j][i] %= mod
            cur = (cur - 1) & i
        
        dp[1][i] = cnt[i]
        for j in range(2, n + 1):
            dp[1][i] -= dp[j][i]
            dp[1][i] %= mod
    
    print('\n'.join(str(dp[i][(1 << n) - 1]) for i in range(1, n + 1)))

# https://codeforces.com/problemset/problem/413/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0410/solution/cf413d.md
#
# 如果是0 则有两种选择，这样ans直接*2 ，ans是之前的ans 转换的时候到2，有两个路径 0->2, 2->2
# 这时候用非1 和非2 记录转换关系
# ndp 用来辅助记录转换结果

from cflibs import *
def main():
    n, k = MII()
    nums = LII()

    total = 1 << k - 1
    dp = [0] * total
    dp[0] = 1

    ndp = [0] * total

    ans = 0
    mod = 10 ** 9 + 7

    for v in nums:
        v //= 2
        
        if v == 0:
            ans += ans
            if ans >= mod:
                ans -= mod
        
        if v != 2:
            for i in range(total - 1):
                ndp[i + 1] += dp[i]
                if ndp[i + 1] >= mod:
                    ndp[i + 1] -= mod
            
            ans += dp[-1]
            if ans >= mod:
                ans -= mod
        
        if v != 1:
            for i in range(1, total, 2):
                ndp[2] += dp[i]
                if ndp[2] >= mod:
                    ndp[2] -= mod
            
            for i in range(0, total - 2, 2):
                ndp[i + 2] += dp[i]
                if ndp[i + 2] >= mod:
                    ndp[i + 2] -= mod
            
            ans += dp[-2]
            if ans >= mod:
                ans -= mod
        
        for i in range(total):
            dp[i] = ndp[i]
            ndp[i] = 0

    print(ans)
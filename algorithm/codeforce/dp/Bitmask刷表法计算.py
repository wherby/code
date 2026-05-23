# https://gemini.google.com/app/8c3fe00a2e02075f
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0402/solution/cf105972m.md
# 原题 逆序对 = K + 偏移量/2 由于偏移量是正负对称，所以在DP的时候，就只取正数就可以获得除2的效果
# algorithm/codeforce/docs/逆序对数目大于偏移量的一半.md 这个形状支持了刷表的时候不用考虑负数值
# 使用刷表的时候，用smaller计算当前位插入的时候引入逆序对的数量，  fmax(bit - cnt, 0) 就是偏移量正值的计算





import init_setting
from cflibs import *
def main(): 
    n, k = MII()
    mod = 10 ** 9 + 7
    
    dp = [[0] * (1 << n) for _ in range(k + 1)]
    dp[0][0] = 1
    
    for i in range(k + 1):
        for j in range(1 << n):
            cnt = j.bit_count()
            smaller = 0
            for bit in range(n):
                if j >> bit & 1: continue
                ni = i + smaller - fmax(bit - cnt, 0)
                nj = j | (1 << bit)
                if ni <= k:
                    dp[ni][nj] += dp[i][j]
                    dp[ni][nj] %= mod
                smaller += 1
    
    print(dp[k][-1])
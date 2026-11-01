# https://codeforces.com/gym/104333/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1019/solution/cf104333b.md
# 计算单独每个位置的贡献
# 状态压缩的时候，每个状态的选取其实对应了一个排列，状态记录了当前选择元素的排列和结果
# algorithm/codeforce/简单/贡献法独立计算.py 虽然也是全排列相关，但是这里的是独立求和，所以会有均匀分布就可以直接求贡献


import init_setting
from cflibs import *
def main():
    n = II()
    v1 = LII()
    v2 = LII()
    
    ans = 0
    mod = 10 ** 9 + 7
    
    empty = [[i for i in range(n) if not msk >> i & 1] for msk in range(1 << n)]
    
    for bit in range(30):
        grid = [[0] * n for _ in range(n)]
        
        for x in range(n):
            for y in range(n):
                grid[x][y] = (v1[x] + v2[y]) >> bit & 1
        
        dp = [[0] * (1 << n) for _ in range(2)]
        dp[0][0] = 1
        
        for msk in range(1 << n):
            x = msk.bit_count()
            for y in empty[msk]:
                for i in range(2):
                    ni = i ^ grid[x][y]
                    nmsk = msk | (1 << y)
                    
                    dp[ni][nmsk] += dp[i][msk]
                    dp[ni][nmsk] %= mod
        
        ans += dp[1][(1 << n) - 1] * (1 << bit) % mod
        ans %= mod
    
    print(ans)
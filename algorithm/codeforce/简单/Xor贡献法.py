# https://codeforces.com/gym/105067/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1229/solution/cf105067f.md
# Xor 计算的贡献法，每位单独计算

import init_setting
from lib.cflibs import *
def main(): 
    n, l, r = MII()
    nums = LII()
    
    cnt = [[0] * 17 for _ in range(2)]
    
    for x in nums:
        for i in range(17):
            cnt[x >> i & 1][i] += 1
    
    M = 1 << 17
    
    vals = [0] * M
    
    for i in range(M):
        for j in range(17):
            vals[i] += cnt[(i >> j & 1) ^ 1][j] << j
    
    vals.sort()
    
    ans = 0
    for i in range(M):
        if i == 0 or vals[i] != vals[i - 1]:
            ans += (r - vals[i]) // (M * n) - (l - 1 - vals[i]) // (M * n)
    
    print(ans)
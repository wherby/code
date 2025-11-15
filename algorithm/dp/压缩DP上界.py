# https://codeforces.com/gym/106188/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1114/solution/cf106188g.md
# M 的值会是 max(nums)*k 但是对于这个题目只需要到达 max(nums) +1 即可，可以把当前的值压缩到最大的这个值就能进行判断了。否则 algorithm/codeforce/dp/test/testDPC.py 就会增加K*2 的复杂度


import init_setting
from lib.cflibs import *
def main(): 
    mod = 10 ** 9 + 7
    
    n, k = MII()
    nums = LII()
    
    nums.sort()
    
    M = 10 ** 4 + 2
    dp = [[0] * M for _ in range(k)]
    dp[0][0] = 1
    
    ans = 0
    
    for i in range(n):
        for j in range(nums[i] + 1, M):
            ans += dp[k - 1][j]
            if ans >= mod:
                ans -= mod
        
        for x in range(k - 2, -1, -1):
            for y in range(M):
                ny = fmin(y + nums[i], M - 1)
                dp[x + 1][ny] += dp[x][y]
                if dp[x + 1][ny] >= mod:
                    dp[x + 1][ny] -= mod
    
    print(ans)
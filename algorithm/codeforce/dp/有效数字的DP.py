# https://codeforces.com/problemset/problem/991/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0812/solution/cf991e.md

import init_setting
from cflibs import *
def main():
    s = I()
    cnt = [0] * 10
    
    for x in s:
        cnt[int(x)] += 1
    
    ans = 0
    
    for digit_cnt in range(1, len(s) + 1):
        dp = [0] * (digit_cnt + 1)
        dp[0] = 1
        
        for i in range(10):
            if cnt[i]:
                ndp = [0] * (digit_cnt + 1)
                for j in range(digit_cnt, 0, -1):
                    for c in range(1, cnt[i] + 1):
                        if j - c < 0: break
                        
                        total = digit_cnt - (j - c)
                        if i == 0: total -= 1
                        
                        if 0 <= c <= total:
                            ndp[j] += dp[j - c] * math.comb(total, c)
                dp = ndp
        
        ans += dp[digit_cnt]
    
    print(ans)
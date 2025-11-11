# https://codeforces.com/gym/106177/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1111/solution/cf106177f.md
# 前缀和求值与当前值奇偶性相关



import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        ans = 0
        
        cnt = [[0] * (2 * n + 5) for _ in range(2)]
        cur = n + 2
        msk = 0
        
        for x in nums:
            cnt[msk][cur] += 1
            
            if x % 2:
                msk ^= 1
                cur -= 1
            else:
                cur += 1
            
            ans += cnt[msk][cur - 1] + cnt[msk ^ 1][cur + 1]
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))

main()
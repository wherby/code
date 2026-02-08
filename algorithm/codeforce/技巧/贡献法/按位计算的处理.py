# https://codeforces.com/gym/104408/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0131/solution/cf104408c.md
# 需要每个字符串相等，通过计算每个位置上是否与前一个字符相等来转换问题，贪心统计每一位上需要翻转的次数，取少的那一边即可
# 因为是反转前缀，所以处理不同的位置是独立的，最后可以保证每个链条的相对值是相同的，最后此链条的值只和最后一个值决定，然后对于此值也可以贪心处理

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        cnt = [0] * m
        
        for _ in range(n):
            s = I()
            
            if int(s[m - 1]):
                cnt[m - 1] += 1
            
            for i in range(m - 1):
                if s[i] != s[i + 1]:
                    cnt[i] += 1
        
        ans = 0
        for i in range(m):
            ans += fmin(cnt[i], n - cnt[i])
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))
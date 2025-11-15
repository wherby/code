# https://codeforces.com/gym/105478/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1112/solution/cf105478b.md
# 在两个确定直接的?。 如果大于2 ，则可以构造一个序列，使得必有一位能命中
# 假设你写了一个序列>2 则只有一个螺旋序列必不命中，则可以调整最后两位，使得其中之一必中。

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        s = I()
        
        ans = 0
        flg = 0
        
        for i in range(n):
            if s[i] != '?':
                ans += 1
                ans += flg
                flg = 0
            elif i and s[i - 1] != '?':
                if i + 1 < n and s[i + 1] != '?' and s[i - 1] != s[i + 1]:
                    ans += 1
                elif i + 1 < n and s[i + 1] == '?':
                    flg = 1
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))
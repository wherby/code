# https://codeforces.com/problemset/problem/1948/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0827/solution/cf1948d.md
# 用从后到前，空间压缩
# if lcp[j] >= j - i: 确保字符串中间字符都被选择

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        s = [ord(c) - ord('a') + 1 if c != '?' else 0 for c in I()]
        n = len(s)
        lcp = [0] * (n + 1)
        
        ans = 0
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[j] == s[i] or s[j] == 0 or s[i] == 0:
                    lcp[j] = lcp[j + 1] + 1
                else:
                    lcp[j] = 0
                if lcp[j] >= j - i:
                    ans = fmax(ans, j - i)
        
        outs.append(ans * 2)
    
    print('\n'.join(map(str, outs)))
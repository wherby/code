
# https://codeforces.com/gym/105780/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1212/solution/cf105780d.md
# 枚举正方形的端点

import init_setting
from lib.cflibs import *
def main(): 
    n = II()
    pts = [tuple(MII()) for _ in range(n)]
    vis = set(pts)
    
    ans = 0
    for i in range(n):
        for j in range(i):
            x1, y1 = pts[i]
            x2, y2 = pts[j]
            
            dx = x2 - x1
            dy = y2 - y1
            
            if (x1 + dx - dy, y1 + dx + dy) in vis and (x1 - dy, y1 + dx) in vis:
                ans += 1
            if (x1 + dy, y1 - dx) in vis and (x1 + dx + dy, y1 + dy - dx) in vis:
                ans += 1
    
    print(ans // 4)
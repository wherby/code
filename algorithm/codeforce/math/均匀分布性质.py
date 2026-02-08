# https://codeforces.com/gym/104020/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0206/solution/cf104020l.md
# 均匀分布的时候，利用生日悖论，点集中在某个区域的概率会大大增加，所以只需要检查距离较近的点对即可，用任意坐标系排序的时候，距离近的点一定会被排在一起

import init_setting
from cflibs import *

def main(): 
    n = II()
    pts = []
    
    for _ in range(n):
        pts.append(tuple(MII()))
    
    pts.sort()
    ans = 4 * 10 ** 18
    
    for i in range(n):
        x1, y1, z1 = pts[i]
        for j in range(fmax(i - 100, 0), i):
            x2, y2, z2 = pts[j]
            ans = fmin(ans, (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1))
    
    print(math.sqrt(ans))
# https://codeforces.com/gym/105198/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0128/solution/cf105198m.md
# 题目中是对x,y 相对关系的分析，
# x,y 是对称等价的，所以可以假设 x >= y
# 然后分析 k 步操作能覆盖的最大距离
# 如果 x 在 k 步内能覆盖 y 的距离，那么直接 x+y 即可
# 否则需要计算多出来的距离，通过每 2k 步可以多覆盖 2 的距离，计算出需要多少额外的 2k 步操作 





import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        sx, sy, tx, ty, k = MII()
        dx = abs(sx - tx)
        dy = abs(sy - ty)
        
        if dx < dy: dx, dy = dy, dx
        
        if dx <= (dy + 1) * k:
            outs.append(dx + dy)
        else:
            other = (dx - (dy + 1) * k + 2 * k - 1) // (2 * k) * 2
            outs.append(dx + dy + other)
    
    print('\n'.join(map(str, outs)))
# https://codeforces.com/gym/104493/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1204/solution/cf104493m.md
#  又因为闵可夫斯基和可交换，所以可以理解为一个正多边形区域的基础上，有一个圆在动。
# 用圆心在多边形边界外形成的面积 等于圆的面积 加上多边形边长 * 圆的半径 + 多边形原始面积 == 多边形在圆的边界平移形成的面积 == 多边形面积 + 圆的面积 + 多变形在圆周移动的面积
# 


import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        r, n, l = MII()
        ans = math.pi * r * r
        ans += l * r * n
        ans += l * l / 2 / math.tan(math.pi / n) * n / 2
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))
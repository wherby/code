# https://codeforces.com/gym/105582/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1022/solution/cf105582k.md
# 首先构造了长度和位置都是整数的多边形坐标，此多边形每条边都是和x,y轴平行，所以可以保证坐标和长度都是整数
# dx, dy = 5, 12 是投影向量，原始长度是整数，此投影向量的长度也是整数？13， 所以保证了在新坐标系下，坐标和长度都是整数
# 奇数的时候，主要是需要处理3这个特殊情况

import init_setting
from cflibs import *
def main(): 
    n = II()
    pts = []
    
    if n % 2:
        pts.append((0, 0))
        
        x, y = 0, 0
        for i in range(n // 2 - 1):
            y += 25
            pts.append((x, y))
            x += 25
            pts.append((x, y))
        
        x = fmax(x, 25)
        pts.append((x, 0))
        pts.append((x // 25 * 9, -x // 25 * 12))
    
    else:
        pts.append((0, 0))
        
        x, y = 0, 0
        for i in range(n // 2 - 1):
            y += 25
            pts.append((x, y))
            x += 25
            pts.append((x, y))
        
        pts.append((x, 0))
    
    dx, dy = 5, 12
    print(pts)
    for x, y in pts:
        print(x * dx + y * dy, x * (-dy) + y * dx)

main()
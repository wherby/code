# https://codeforces.com/gym/105297/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0819/solution/cf105297d.md
# 这个题目最大的问题是第一个求和你要放入球的相对位置很难判断
# 这里利用了对称等价性，通过旋转的方式，让第一个球一定位于内侧，这时与轴平面相交的时候，一定能放最大的球
# 这时就可推断出新球的坐标是和半径相关的，然后计算两球相切的情况是否能成立二分大小

import init_setting
from cflibs import *
def main():
    x, y, z = MII()
    tx, ty, tz = LFI()
    R = LFI()[0]
    
    tx = fmax(tx, x - tx)
    ty = fmax(ty, y - ty)
    tz = fmax(tz, z - tz)
    
    l, r = 0, min(x, y, z) / 2
    
    for _ in range(100):
        mid = (l + r) / 2
        if math.hypot(tx - mid, ty - mid, tz - mid) >= R + mid:
            l = mid
        else:
            r = mid
    
    print((l + r) / 2)
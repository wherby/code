# https://codeforces.com/problemset/problem/203/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0821/solution/cf203d.md
# 运动反射的时候，第一次是镜像，第二次则是同向，所以用2倍取余

import init_setting
from lib.cflibs import *
def main():
    a, b, m = MII()
    vx, vy, vz = MII()
    
    time = -m / vy
    
    x = a / 2 + vx * time
    z = vz * time
    
    x %= 2 * a
    z %= 2 * b
    
    if x >= a: x = 2 * a - x
    if z >= b: z = 2 * b - z
    print(x, z)
# https://codeforces.com/gym/106045/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1210/solution/cf106045d.md
# 边在圆盘上投影就是角度对应的圆环上的弦长，用三角形公式得到长度，距离和弦长构成直角三角形，边就是连接线长度


import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        r, l, theta = LII()
        theta = theta / 180 * math.pi
        w = 2 * r * math.sin(theta / 2)
        outs.append(math.sqrt(l * l - w * w))
    
    print('\n'.join(map(str, outs)))
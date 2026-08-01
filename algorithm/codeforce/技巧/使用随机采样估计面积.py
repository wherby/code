# https://codeforces.com/gym/104670/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0725/solution/cf104670g.md
# 这里使用随机采样估计面积大小，其实如果点数小的话，可以直接用枚举所以点？ 用0.1步长的细分网格就可以

import init_setting
from cflibs import *
def main():
    n = II()
    xs = []
    ys = []
    rs = []
    
    for _ in range(n):
        x, y, r = MII()
        xs.append(x)
        ys.append(y)
        rs.append(r)
    
    import time
    t = time.time()
    
    freq = 0
    total = 0
    
    while time.time() - t < 2.5:
        x = random.random() * 30 - 10
        y = random.random() * 30 - 10
        
        total += 1
        for i in range(n):
            vx = xs[i]
            vy = ys[i]
            r = rs[i]
            
            if (x - vx) * (x - vx) + (y - vy) * (y - vy) <= r * r:
                freq += 1
                break
    
    print(freq / total * 900)
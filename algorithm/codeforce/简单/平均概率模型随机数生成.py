# https://codeforces.com/gym/105122/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1022/solution/cf105122a.md
# 其实平均概率模型下，可以在二维平面上取一半的点输出即可

import init_setting
from lib.cflibs import *
def main():
    k = II()
    n = II()
    
    outs = []
    
    for _ in range(n):
        if random.randint(1, k * (k + 1) // 2) <= k:
            x = random.randint(1, k)
            outs.append(f'{x} {x}')
        else:
            while True:
                x = random.randint(1, k)
                y = random.randint(1, k)
                if x != y: break
            if x > y: x, y = y, x
            outs.append(f'{x} {y}')
    
    print('\n'.join(outs))
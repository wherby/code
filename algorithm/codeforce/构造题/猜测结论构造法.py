# https://codeforces.com/gym/106687/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0909/solution/cf106687c.md
# 投影面积最大的 完全覆盖的构造法

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        a, b, c = MII()
        mi = min(a, b, c)
        
        if a == mi:
            outs.append(str(b * c))
            for i in range(1, b + 1):
                for j in range(1, c + 1):
                    outs.append(f'{(i + j) % a + 1} {i} {j}')
        
        elif b == mi:
            outs.append(str(a * c))
            for i in range(1, a + 1):
                for j in range(1, c + 1):
                    outs.append(f'{i} {(i + j) % b + 1} {j}')
        
        else:
            outs.append(str(a * b))
            for i in range(1, a + 1):
                for j in range(1, b + 1):
                    outs.append(f'{i} {j} {(i + j) % c + 1}')
    
    print('\n'.join(outs))
# https://codeforces.com/gym/106414/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0506/solution/cf106414j.md
# 在已知点上加入构造点，使得封闭连线不会有共线的三个点的简单图形
# 这里有两种情况，如果前后两点x不变，则此构造会由于y增大变成y轴上向右下的锯齿，如果x变化，则差值至少是1，则变成x轴上向右下方向的锯齿，然后加上y轴很大的封口，构造成简单的封闭图形 

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    step = 2 * 10 ** 8 + 5
    
    for _ in range(t):
        n = II()
        pts = []
        
        for _ in range(n):
            x, y = MII()
            pts.append((x, y))
        
        pts.sort()
        
        ans = []
        
        for x, y in pts:
            ans.append(f'{x} {y}')
            ans.append(f'{x + 1} {y - step}')
        
        ans.append(f'{step} {step}')
        ans.append(f'{-step} {step}')
        
        outs.append(str(len(ans)))
        outs.append('\n'.join(ans))
    
    print('\n'.join(outs))
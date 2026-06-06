# https://codeforces.com/gym/103150/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0603/solution/cf103510d.md
# 有个隐形的结论，在正方形点中，最小的最大距离移动构造




import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, d = MII()
        
        if (n // 2) * (n // 2) * 2 >= d:
            outs.append('YES')
            
            x = n // 2 * 2
            for i in range(x):
                for j in range(x):
                    outs.append(f'{i + 1} {j + 1} {(i + x // 2) % x + 1} {(j + x // 2) % x + 1}')
            
            if n % 2:
                for i in range(1, n + 1):
                    outs.append(f'{i} {n} {n} {n + 1 - i}')
                
                for i in range(1, n):
                    outs.append(f'{n} {i} {n - i} {n}')
        else:
            outs.append('NO')
    
    print('\n'.join(outs))
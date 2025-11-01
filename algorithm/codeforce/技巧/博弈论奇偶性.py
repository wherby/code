# https://codeforces.com/gym/106144/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1031/solution/cf106144f.md
# 不同类型操作。偶数可以镜像操作同一类型，


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        c0 = 0
        c1 = 0
        
        for _ in range(n):
            s = I()
            if 'xxx' in s: c1 ^= 1
            elif 'xx' in s: c0 ^= 1
        
        outs.append('Monocarp' if c1 or c1 else 'Polycarp')
    
    print('\n'.join(outs))
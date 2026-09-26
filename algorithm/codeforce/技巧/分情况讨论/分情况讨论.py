# https://codeforces.com/gym/102873/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0907/solution/cf102873f.md
# 列举情况计算。。


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        if n % 4 == 0: outs.append('Draw')
        elif n % 4 == 2: outs.append('Alice')
        else: outs.append('Bob')
    
    print('\n'.join(outs))
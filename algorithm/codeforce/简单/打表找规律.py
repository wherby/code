# https://codeforces.com/gym/104147/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0205/solution/cf104147d.md
# 打表找规律，
# 后手的时候，一定能构成(k+1) 的倍数


import init_setting
from lib.cflibs import *
def main(): 
    fin = open('dotak.in', 'r')
    input = lambda: fin.readline().strip()
    
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        v = n * k % (k + 1)
        outs.append('Omda' if v % 2 or v == k else 'Teemo')
    
    print('\n'.join(outs))
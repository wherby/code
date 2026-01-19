# https://codeforces.com/gym/104064/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0117/solution/cf104064d.md
# 对角线连接优于垂直连接的时候的优化和特殊情况考虑




import init_setting
from lib.cflibs import *
def main(): 
    n = II()
    inf = 10 ** 9
    
    add_ma = -inf
    add_mi = inf
    minus_ma = -inf
    minus_mi = inf
    
    for _ in range(n):
        x, y = MII()
        add_ma = fmax(add_ma, x + y)
        add_mi = fmin(add_mi, x + y)
        minus_ma = fmax(minus_ma, x - y)
        minus_mi = fmin(minus_mi, x - y)
    
    if add_ma == add_mi and minus_ma == minus_mi:
        print(4)
    elif add_ma == add_mi or minus_ma == minus_mi:
        print(add_ma - add_mi + minus_ma - minus_mi + 5)
    else:
        print(add_ma - add_mi + minus_ma - minus_mi + 4)
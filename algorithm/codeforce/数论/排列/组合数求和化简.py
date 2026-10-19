# https://codeforces.com/gym/102829/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1016/solution/cf102829i.md
# algorithm/mathA/combination/docs/组合数求和化简.md

import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main():
    mod = 10 ** 9 + 7
    f = Factorial(2 * 10 ** 6 + 5, mod)
    
    t = II()
    outs = []
    
    for _ in range(t):
        x, y = MII()
        x = abs(x) + 1
        y = abs(y) + 1
        outs.append(f.combi(x + y, x) - 1)
    
    print('\n'.join(map(str, outs)))
# https://codeforces.com/gym/101962/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0617/solution/cf101962c.md
# 考虑贡献法， 在长度为L的区间选取了前后端点 最大值和最小值的差值L—1，这样的区间有 N-L+1个，区间内选择有2**(L-2)种。
# 然后变成一个算术级数的多项式求和，需要用算术级数求和公式化简
# algorithm/codeforce/docs/AGP算术级数求和公式化简.md


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        n = II()
        outs.append((pow(2, n, mod) * (n - 3) % mod + n + 3) % mod)
    
    print('\n'.join(map(str, outs)))

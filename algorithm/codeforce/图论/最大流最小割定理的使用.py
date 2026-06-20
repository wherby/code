# https://codeforces.com/gym/105442/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0616/solution/cf105442k.md
# 根据 最大流最小割定理（Max-Flow Min-Cut Theorem），要让 $S$ 和 $E$ 完全断开，所有可能的切断方案（割）的容量极小值就是该分段的最大流。
# algorithm/codeforce/docs/最大流最小割定理.md

import init_setting
from cflibs import *
def main():
    n = II()
    ans = 10 ** 9
    
    for _ in range(n):
        a, b, c, d, e = MII()
        ans = fmin(ans, min(a + d, b + e, a + c + e, b + c + d))
    
    print(ans)
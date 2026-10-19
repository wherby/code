# https://codeforces.com/gym/106744/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1007/solution/cf106744g.md
# 因为知道最大值，然后预填最大值，然后贪心求剩余值的背包，因为连续值背包一定有解

import init_setting
from lib.cflibs import *
def main():
    n, k = MII()
    
    v = k * (k + 1) // 2
    mx = (n + v - 1) // v
    
    ans = [mx] * k
    resid = mx * v - n
    
    for i in range(k - 1, -1, -1):
        x = fmin(resid // (i + 1), mx)
        ans[i] -= x
        resid -= (i + 1) * x
    
    print(' '.join(map(str, ans)))
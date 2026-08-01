# https://codeforces.com/gym/102767/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0722/solution/cf102767g.md
# 因为其模n 余1 的最小数组长度
# n不是质数，如果当前数字与n不互质，则之后乘积用于不会余1，所以会产生断裂，需要清楚前面数字的影响

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []

    for _ in range(t):
        n = II()
        nums = LII()
        
        if n == 1:
            outs.append(0)
            continue
        
        ans = n + 1
        
        vis = [-2] * n
        
        cur = 1
        vis[1] = -1
        tmp = [1]
        
        for i in range(n):
            if math.gcd(n, nums[i]) > 1:
                for x in tmp:
                    vis[x] = -2
                cur = 1
                vis[1] = i
                tmp = [1]
            else:
                cur = cur * nums[i] % n
                if vis[cur] != -2: ans = fmin(ans, i - vis[cur])
                else: tmp.append(cur)
                vis[cur] = i
        
        outs.append(ans if ans <= n else 0)

    print('\n'.join(map(str, outs)))
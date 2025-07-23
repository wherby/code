# https://codeforces.com/problemset/problem/370/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0722/solution/cf370c.md
# 构造不相等的队列，找打最大偏差值，然后应用偏差

import init_setting
from lib.cflibs import *
def main():
    n, k = MII()
    nums = LII()
    
    cnt = [0] * (k + 1)
    for v in nums:
        cnt[v] += 1
    
    ma = max(cnt)
    
    nums.sort()
    
    print(fmin(n, 2 * n - 2 * ma))
    print('\n'.join(f'{nums[i]} {nums[(i + ma) % n]}' for i in range(n)))
# https://codeforces.com/problemset/problem/746/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0708/solution/cf746e.md
# 先按照条件做完在判定条件
# 在预处理的时候，按照最终选择？从大到小改，先选 一半出来
# 

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n, k = MII()
    nums = LII()

    vis0 = set()
    vis1 = set()

    v = n // 2
    chosen = [0] * n

    for i in sorted(range(n), key=lambda x: -nums[x]):
        s = str(nums[i])
        if nums[i] % 2:
            if len(vis1) < v and s not in vis1:
                vis1.add(s)
                chosen[i] = 1
        else:
            if len(vis0) < v and s not in vis0:
                vis0.add(s)
                chosen[i] = 1

    ans = 0
    v0 = 2
    v1 = 1
    ma_val = 0

    for i in range(n):
        if not chosen[i]:
            if len(vis1) < v:
                while str(v1) in vis1:
                    v1 += 2
                nums[i] = v1
                vis1.add(str(v1))
            else:  # if len(vis1) < v: 其实不需要，因为在choosen 的时候就标记了， 而且奇数偶数原先的candidate不一定都过半，所有先把一个填完再填另一个也是可以的
                while str(v0) in vis0:
                    v0 += 2
                nums[i] = v0
                vis0.add(str(v0))
            
            ma_val = fmax(ma_val, nums[i])
            ans += 1


    if ma_val > k: print(-1)
    else:
        print(ans)
        print(*nums)
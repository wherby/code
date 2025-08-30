# https://codeforces.com/problemset/problem/1970/B2
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0820/solution/cf1970b2.md
# 这里对距离先大后小排序，然后强制使得排序后的x位置相邻,形成当前的点和上一个点的x距离恒为1，达到方便计算yi距离差的目的
# 1 <= ys[last_idx] + nums[idx] <= n: 这里就是在计算下一个点的距离,因为和上一个点的x距离恒定为1，已经减去，如果增加y值不行就减少
# nums[idx] < 0， 如果距离为0 的时候，移动的点就是本身点，不能移动到上一个距离

import init_setting
from lib.cflibs import *
def main():
    n = II()
    nums = LII()
    st_range = sorted(range(1, n), key=lambda x: -nums[x])
    
    xs = [1] * n
    ys = [1] * n
    
    target = [0] * n
    
    last_idx = 0
    for i in range(n - 1):
        idx = st_range[i]
        nums[idx] -= 1
        
        xs[idx] = xs[last_idx] + 1
        if 1 <= ys[last_idx] + nums[idx] <= n:
            ys[idx] = ys[last_idx] + nums[idx]
        else:
            ys[idx] = ys[last_idx] - nums[idx]
        
        if nums[idx] < 0: target[idx] = idx
        else: target[idx] = last_idx
        
        last_idx = idx
    
    print('YES')
    print('\n'.join(f'{xs[i]} {ys[i]}' for i in range(n)))
    print('\n'.join(str(x + 1) for x in target))
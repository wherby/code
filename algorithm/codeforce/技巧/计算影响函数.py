# https://codeforces.com/problemset/problem/1889/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0618/solution/cf1889b.md
# 按照题意，一定是用1去连接其他点，但是其他点的连接顺序可以按照连接这个点对左右影响得到计算出 idx*c , nums[idx] 所以相减排序就可以贪心解决

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    t = II()
    outs = []

    for _ in range(t):
        n, c = MII()
        nums = LII()
        
        st_range = sorted(range(1, n), key=lambda x: x * c - nums[x])
        
        cur = nums[0]
        flg = True
        
        for i in st_range:
            if cur + nums[i] >= c * (i + 1): cur += nums[i]
            else: flg = False
        
        outs.append('Yes' if flg else 'No')

    print('\n'.join(outs))
# https://codeforces.com/gym/106020/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0630/solution/cf106020f.md
# 有奇偶两种情况：
# 如果是偶数，肯定选最大的
# 如果是奇数，则可以用最小后悔思想，如果后面还有K次，k 次都是偶数，如果当前的奇数最大值 在最差的情况下比最后一个偶数大，则奇数最大值这时选择就不会后悔，就应该选，否则选偶数最大值


import init_setting
from cflibs import *
def main():
    n, k = MII()
    nums = LII()
    
    idxs1 = list(range(0, n, 2))
    idxs2 = list(range(1, n, 2))
    
    idxs1.sort(key=lambda x: nums[x])
    idxs2.sort(key=lambda x: nums[x])
    
    def output(x):
        print(x + 1, flush=True)
        II()
    
    for i in range(k):
        v = II()
        
        if v == 1:
            resid = k - i
            if nums[idxs1[-1]] >= nums[idxs2[-resid]]:
                output(idxs1.pop())
            else:
                output(idxs2.pop())
        else:
            output(idxs2.pop())
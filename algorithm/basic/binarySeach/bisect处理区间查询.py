
# idx = bisect_right(nums, tar, a, b + 1) - 1 [处理查找区间,如果tar 小于 nums[a]的值，返回a,如果大于nums[b],返回 b+1,最后-1， 这里是对一个前闭后开的区间搜索，b+1是最后可以被插入的index](contest/00000c490d177/d181/q4/t4.py)

# def bisect_right(a, x, lo=0, hi=None, *, key=None):
#     """Return the index where to insert item x in list a, assuming a is sorted.

#     The return value i is such that all e in a[:i] have e <= x, and all e in
#     a[i:] have e > x.  So if x already appears in the list, a.insert(i, x) will
#     insert just after the rightmost x already there.

#     Optional args lo (default 0) and hi (default len(a)) bound the
#     slice of a to be searched.

#     A custom key function can be supplied to customize the sort order.
#     """

# https://leetcode.cn/contest/biweekly-contest-181/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/description/
from typing import List, Tuple, Optional


from bisect import bisect_right,insort_left,bisect_left




class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + (1 if nums[i] % 2 == 0 else 0)
        
        ans = []
        
        for a,b,k in queries:
            l = 1
            r = k  + 10**6
            re = -1
            while l <= r:
                mid = (l + r) // 2
                tar = 2 * mid
                idx = bisect_right(nums, tar, a, b + 1) - 1
                removed = 0
                if idx >= a:
                    removed = pre[idx + 1] - pre[a]
                remaining = mid - removed
                
                if remaining >=k:
                    re = mid
                    r = mid - 1
                else:
                    l = mid +1
            
            ans.append(re*2)
        return ans 



re =Solution().kthRemainingInteger(nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]])
print(re)
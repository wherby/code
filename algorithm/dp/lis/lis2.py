from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        pre = self.getLISArray(nums)
        suf = self.getLISArray(nums[::-1])[::-1]
        ans = 0

        for pre_i, suf_i in zip(pre, suf):
            if pre_i > 1 and suf_i > 1:
                ans = max(ans, pre_i + suf_i - 1)
        
        return len(nums) - ans

    def getLISArray(self, nums: List[int]) -> List[int]:
        dp, seq = list(), list()

        for i, num in enumerate(nums):
            it = bisect_left(seq, num)
            if it == len(seq):
                seq.append(num)
                dp.append(len(seq))
            else:
                seq[it] = num
                dp.append(it + 1)

        return dp

#作者：力扣官方题解
#链接：https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/solutions/2570598/zui-chang-di-zeng-zi-xu-lie-by-leetcode-2ipno/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
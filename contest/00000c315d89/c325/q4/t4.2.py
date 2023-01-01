from typing import List, Tuple, Optional
from functools import cache

mod = 10 ** 9 + 7
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k: return 0
        n = len(nums)
        tot_method = pow(2, n, mod)
        @cache
        def getRes(idx, space):
            if idx == n: return 1
            res = getRes(idx+1, space)
            if nums[idx] <= space: res += getRes(idx+1, space-nums[idx])
            return res % mod
        ans = (tot_method - getRes(0, k-1) * 2) % mod
        getRes.cache_clear()
        return ans

#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/RmydJj/view/cYCjYk/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
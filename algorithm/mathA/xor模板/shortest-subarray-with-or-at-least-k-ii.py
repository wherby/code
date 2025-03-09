# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/solutions/2716483/zi-shu-zu-orandgcd-tong-yong-mo-ban-pyth-n8xj/
from typing import List, Tuple, Optional
from math import inf

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        d = dict()
        for i, x in enumerate(nums):
            #print("a",d.items())  # 隐含条件，d.items()会返回顺序插入的元素
            d = {or_ | x: left for or_, left in d.items()}
            #print(d)
            d[x] = i  # 只包含 x 的子数组
            #print(d)
            for or_, left in d.items():
                if or_ >= k:
                    ans = min(ans, i - left + 1)
        return ans if ans < inf else -1

#作者：灵茶山艾府
#链接：https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/solutions/2716483/zi-shu-zu-orandgcd-tong-yong-mo-ban-pyth-n8xj/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

re = Solution().minimumSubarrayLength([6,4,2,5,8,7,4,21,1],7)
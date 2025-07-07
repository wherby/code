from math import inf
from typing import List, Tuple, Optional
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            j = i - 1
            # 如果 x 是 nums[j] 的子集，就退出循环
            while j >= 0 and nums[j] | x != nums[j]:
                nums[j] |= x
                ans = min(ans, abs(nums[j] - k))
                j -= 1
            print(nums[max(0,i-1-30):i+1])
            #print(nums)
        return ans

nums  =[1<<(i//3) for i in range(30)]
#print(nums)
re = Solution().minimumDifference(nums, (1<<10)-1)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/solutions/2798206/li-yong-and-de-xing-zhi-pythonjavacgo-by-gg4d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# https://leetcode.cn/problems/smallest-subarrays-with-maximum-bitwise-or/solutions/1830911/by-endlesscheng-zai1/?envType=daily-question&envId=2025-07-29
from typing import List, Tuple, Optional
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)  # 子数组的长度至少是 1
        for i, x in enumerate(nums):  # 计算右端点为 i 的子数组的或值
            for j in range(i - 1, -1, -1):
                if (nums[j] | x) == nums[j]:  # nums[j] 及其左边元素无法增大
                    break
                nums[j] |= x  # nums[j] 增大，现在 nums[j] = 原数组 nums[j] 到 nums[i] 的或值
                ans[j] = i - j + 1  # nums[j] 最后一次增大时的子数组长度就是答案
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/smallest-subarrays-with-maximum-bitwise-or/solutions/1830911/by-endlesscheng-zai1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

re  = Solution().smallestSubarrays(nums = [1,0,2,1,3])
print(re)
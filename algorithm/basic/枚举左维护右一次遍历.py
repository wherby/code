from typing import List, Tuple, Optional

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = max_diff = pre_max = 0
        for x in nums:
            ans = max(ans, max_diff * x)
            max_diff = max(max_diff, pre_max - x)
            pre_max = max(pre_max, x)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/solutions/2464857/mei-ju-jzhao-qian-hou-zui-da-zhi-pythonj-um8q/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
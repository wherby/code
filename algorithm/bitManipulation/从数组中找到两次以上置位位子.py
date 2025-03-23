# https://leetcode.cn/problems/maximum-or/description/?envType=daily-question&envId=2025-03-21
from typing import List, Tuple, Optional
#fixed 这个运算可以找到数组中两次以上置位的位置为1

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        all_or = fixed = 0
        for x in nums:
            # 如果在计算 all_or |= x 之前，all_or 和 x 有公共的 1
            # 那就意味着有多个 nums[i] 在这些比特位上都是 1
            fixed |= all_or & x  # 把公共的 1 记录到 fixed 中
            all_or |= x  # 所有数的 OR
        return max((all_or ^ x) | fixed | (x << k) for x in nums)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-or/solutions/2268795/tan-xin-qian-hou-zhui-fen-jie-pythonjava-wrv1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
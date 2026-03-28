
from typing import List, Tuple, Optional

class Solution:
    def countGoodSubarrays(self, nums: List[int]) -> int:
        or_left = []  # (子数组或值，最小左端点)
        last = {}
        ans = 0

        for i, x in enumerate(nums):
            last[x] = i

            # 计算以 i 为右端点的子数组或值
            for p in or_left:
                p[0] |= x
            # x 单独一个数作为子数组
            or_left.append([x, i])

            # 原地去重（相同或值只保留最左边的）
            # 原理见力扣 26. 删除有序数组中的重复项
            idx = 1
            for j in range(1, len(or_left)):
                if or_left[j][0] != or_left[j - 1][0]:
                    or_left[idx] = or_left[j]
                    idx += 1
            del or_left[idx:]

            for k, (or_val, left) in enumerate(or_left):
                right = or_left[k + 1][1] - 1 if k < len(or_left) - 1 else i
                # 对于左端点在 [left, right]，右端点为 i 的子数组，OR 值都是 or_val
                j = last.get(or_val, -1)
                if j >= left:
                    ans += min(right, j) - left + 1

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-good-subarrays/solutions/3933380/mo-ban-logtrick-ji-lu-mei-ge-yuan-su-de-otgcv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
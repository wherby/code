# 
# SOS DP (高维前缀和DP,可以通过降1维的方式递推)
# 因为 状态 1111 可以由 0111， 1011,1101,1110 子集覆盖，所以状态转移由 子集而来
# 子集也是由子集的子集状态合成而来，
# 所以 1111 状态 已经包含了 14个子集状态
# 使用场景： 状态A是完全优于状态A的子状态，则状态A可以由最近级别的子状态优化递推
from typing import List, Tuple, Optional

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        w = max(nums).bit_length()
        u = 1 << w
        f = [0] * u
        for x in nums:
            f[x] = x

        for i in range(w):
            j = 0
            while j < u:
                j |= 1 << i  # 快速跳到第 i 位是 1 的 j
                v = f[j ^ (1 << i)]
                if v > f[j]:
                    f[j] = v  # 手写 max 更快
                j += 1

        return max(x * f[(u - 1) ^ x] for x in nums)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-product-of-two-integers-with-no-common-bits/solutions/3768219/mo-ban-gao-wei-qian-zhui-he-sos-dppython-78fz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
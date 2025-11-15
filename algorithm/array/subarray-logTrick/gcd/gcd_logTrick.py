# https://leetcode.cn/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/solutions/2241277/liang-chong-fang-fa-bao-li-mei-ju-li-yon-refp/?envType=daily-question&envId=2025-11-12
from typing import List, Tuple, Optional
from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if gcd(*nums) > 1:
            return -1
        n = len(nums)
        cnt1 = sum(x == 1 for x in nums)
        if cnt1:
            return n - cnt1

        min_size = n
        a = []  # [GCD，相同 GCD 闭区间的右端点]
        for i, x in enumerate(nums):
            a.append([x, i])

            # 原地去重，因为相同的 GCD 都相邻在一起
            j = 0
            for p in a:
                p[0] = gcd(p[0], x)
                if a[j][0] != p[0]:
                    j += 1
                    a[j] = p
                else:
                    a[j][1] = p[1]
            del a[j + 1:]

            if a[0][0] == 1:
                # 这里本来是 i-a[0][1]+1，把 +1 提出来合并到 return 中
                min_size = min(min_size, i - a[0][1])
        return min_size + n - 1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/solutions/2241277/liang-chong-fang-fa-bao-li-mei-ju-li-yon-refp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
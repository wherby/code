# https://leetcode.cn/problems/minimum-stability-factor-of-array/submissions/641704624/

from typing import List, Tuple, Optional
import math
from bisect import bisect_right,insort_left,bisect_left



class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        def check(upper: int) -> bool:
            intervals = []  # (子数组 GCD，最小左端点)
            c = maxC
            for i, x in enumerate(nums):
                # 计算以 i 为右端点的子数组 GCD
                for p in intervals:
                    p[0] = math.gcd(p[0], x)
                # nums[i] 单独一个数作为子数组
                intervals.append([x, i])

                # 去重（合并 GCD 相同的区间）
                idx = 1
                for j in range(1, len(intervals)):
                    if intervals[j][0] != intervals[j - 1][0]:
                        intervals[idx] = intervals[j]
                        idx += 1
                del intervals[idx:]

                # intervals 的性质：越靠左，GCD 越小

                # 我们只关心 GCD >= 2 的子数组
                if intervals[0][0] == 1:
                    intervals.pop(0)

                # intervals[0] 的 GCD >= 2 且最长，取其区间左端点作为子数组的最小左端点
                if intervals and i - intervals[0][1] + 1 > upper:
                    if c == 0:
                        return False
                    c -= 1
                    intervals.clear()  # 修改后 GCD 均为 1，直接清空
            return True

        return bisect_left(range(len(nums) // (maxC + 1)), True, key=check)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-stability-factor-of-array/solutions/3716266/er-fen-da-an-logtrickpythonjavacgo-by-en-jqxy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from v5input import nums,maxC
#re = Solution().minStable(nums,maxC)
re = Solution().minStable([2,4,9,6],1)
print(re)
# https://leetcode.cn/problems/maximize-subarray-gcd-score/solutions/3695642/liang-chong-xie-fa-bao-li-mei-ju-logtric-zz7e/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from math import gcd

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        lowbit_pos = defaultdict(list)

        ans = 0
        intervals = []  # 每个元素是一个三元组 (g, l, r)，表示区间 (l, r] 的 GCD 为 g
        for i, x in enumerate(nums):
            lowbit_pos[x & -x].append(i)

            # 更新已有区间的 GCD
            for p in intervals:
                p[0] = gcd(p[0], x)
            # 添加新元素作为新区间
            intervals.append([x, i - 1, i])

            # 去重（合并 g 相同的区间）
            idx = 1
            for j in range(1, len(intervals)):
                if intervals[j][0] != intervals[j - 1][0]:
                    intervals[idx] = intervals[j]
                    idx += 1
                else:
                    intervals[idx - 1][2] = intervals[j][2]
            del intervals[idx:]

            # 此时我们将区间 [0,i] 划分成了 len(intervals) 个左开右闭区间
            # 对于 intervals 中的 (l,r]，对于任意 j∈(l,r]，gcd(区间[j,i]) 的计算结果均为 g
            for g, l, r in intervals:
                # 不做任何操作
                ans = max(ans, g * (i - l))
                # 看看能否乘 2
                pos = lowbit_pos[g & -g]
                min_l = max(l, pos[-k - 1]) if len(pos) > k else l
                if min_l < r:  # 可以乘 2
                    ans = max(ans, g * 2 * (i - min_l))

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximize-subarray-gcd-score/solutions/3695642/liang-chong-xie-fa-bao-li-mei-ju-logtric-zz7e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
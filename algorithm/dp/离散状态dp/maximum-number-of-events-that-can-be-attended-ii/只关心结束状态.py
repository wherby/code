from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left

# 手写 max 更快
max = lambda a, b: b if b > a else a


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda e: e[1])  # 按照结束时间排序
        n = len(events)
        f = [[0] * (k + 1) for _ in range(n + 1)]
        for i, (start_day, _, value) in enumerate(events):
            p = bisect_left(events, start_day, hi=i, key=lambda e: e[1])  # hi=i 表示二分上界为 i（默认为 n）
            for j in range(1, k + 1):
                # 为什么是 p 不是 p+1：上面算的是 >= start_day，-1 后得到 < start_day，但由于还要 +1，抵消了
                f[i + 1][j] = max(f[i][j], f[p][j - 1] + value)
        return f[n][k]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/solutions/1913087/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-fuip/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

re = Solution().maxValue([[41,54,68],[28,84,88],[35,44,51],[10,64,36],[81,86,25],[6,51,80],[17,99,35],[8,86,22],[82,89,60],[61,73,96],[50,52,28]],11)
print(re)
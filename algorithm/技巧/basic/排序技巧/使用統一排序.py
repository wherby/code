# 这里有几个技巧：
# bisect_left(a, (l,), hi=i)   这里因为要求当前 l 上有一个，而排序是 双变量，所以使用 (l,)作为排序变量，则会得到当前 l前一个的位置  （l,)并不是排序的默认值是0，而是(l,) 表示一个一维 tuple 变量
# 因为求 （sum,(idx))的二维偏序变量，sum升序，idx 降序，所以把sum变成负值，则变成统一降序

from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        a = [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
        a.sort(key=lambda t: t[0])  # 按照右端点排序
        f = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]
        for i, (r, l, weight, idx) in enumerate(a):
            k = bisect_left(a, (l,), hi=i)  # hi=i 表示二分上界为 i（默认为 n）
            for j in range(1, 5):
                # 为什么是 f[k] 不是 f[k+1]：上面算的是 >= l，-1 后得到 < l，但由于还要 +1，抵消了
                s2, id2 = f[k][j - 1]
                # 注意这里是减去 weight，这样取 min 后相当于计算的是最大和
                f[i + 1][j] = min(f[i][j], (s2 - weight, sorted(id2 + [idx])))
        return f[-1][4][1]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-score-of-non-overlapping-intervals/solutions/3039058/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-wmuy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
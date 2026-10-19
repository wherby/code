# https://leetcode.cn/problems/minimum-interval-selection-to-cover-target-intervals/description/
# while cur_end < tar_r: 这里就把单点情况去除了
from typing import List, Tuple, Optional
class Solution:
    # 56. 合并区间
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序

        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:  # 左端点在合并区间内，可以合并
                ans[-1][1] = max(ans[-1][1], p[1])  # 更新合并区间的右端点
            else:  # 不相交，无法合并
                ans.append(p)  # 新的合并区间
        return ans

    def minSelection(self, availableIntervals: list[list[int]], targetIntervals: list[list[int]]) -> int:
        availableIntervals.sort(key=lambda p: p[0])

        cur_end = 0  # 已建造的桥的右端点
        next_end = 0  # 下一座桥的右端点的最大值
        ans = i = 0
        for tar_l, tar_r in self.merge(targetIntervals):
            while cur_end < tar_r:
                # 当前最靠左的未覆盖位置
                uncover = max(tar_l, cur_end)

                # 寻找下一座桥的最远点
                while i < len(availableIntervals) and availableIntervals[i][0] <= uncover:
                    next_end = max(next_end, availableIntervals[i][1])
                    i += 1

                # 无法覆盖 uncover，或者无法继续向右延伸
                if next_end < uncover or next_end == uncover < tar_r:
                    return -1

                cur_end = next_end  # 建桥后，最远可以到达 next_end
                ans += 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-interval-selection-to-cover-target-intervals/solutions/4045141/qu-jian-he-bing-qu-jian-fu-gai-pythonjav-05u0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
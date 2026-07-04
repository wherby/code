# https://leetcode.cn/contest/weekly-contest-508/problems/filter-occupied-intervals/description/
# 在去除的时候，用两个if 解决了3种可能相交情况
from typing import List, Tuple, Optional

class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.sort(key=lambda x: x[0])
        merged = []
        for l, r in occupiedIntervals:
            if not merged or merged[-1][1] + 1 < l:
                merged.append([l, r])
            else:
                if r > merged[-1][1]:
                    merged[-1][1] = r
        ans = []
        for l, r in merged:
            if r < freeStart or l > freeEnd:
                ans.append([l, r])
            else:
                if l < freeStart:
                    ans.append([l, freeStart - 1])
                if r > freeEnd:
                    ans.append([freeEnd + 1, r])
        return ans
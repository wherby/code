# https://leetcode.cn/problems/maximum-capacity-within-budget/description/
from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        st = [(0,0)]
        ls = [(c,cap) for c,cap in zip(costs,capacity)]
        ls.sort()
        ret = 0
        for c,cap in ls:
            if c >= budget:continue
            k = bisect_left(st,(budget-c  ,0))
            ret = max(ret,cap + st[k-1][1])
            #print(ret,st,k,c,cap)
            if cap > st[-1][1]:
                st.append((c,cap))
        return ret
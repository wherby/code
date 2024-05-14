# https://leetcode.cn/problems/total-cost-to-hire-k-workers/?envType=daily-question&envId=2024-05-01
# heapify heapify a slice which will not impact the original array  // slice will not impact original array
# heapreplace method replace top value of heap with new value

from typing import List, Tuple, Optional

from heapq import heapify,heapreplace
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 + k > n:
            # 也可以 sum(nsmallest(k, costs))，但效率不如直接排序
            costs.sort()
            return sum(costs[:k])

        pre = costs[:candidates]
        suf = costs[-candidates:]
        heapify(pre)
        heapify(suf)
        #print(pre,costs)

        ans = 0
        i = candidates
        j = n - 1 - candidates
        for _ in range(k):
            if pre[0] <= suf[0]:
                ans += heapreplace(pre, costs[i])
                i += 1
            else:
                ans += heapreplace(suf, costs[j])
                j -= 1
        return ans
    
re = Solution().totalCost([25,65,41,31,14,20,59,42,43,57,73,45,30,77,17,38,20,11,17,65,55,85,74,32,84],24,8)
print(re)
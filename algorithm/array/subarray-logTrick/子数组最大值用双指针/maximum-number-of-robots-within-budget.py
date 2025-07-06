from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        pre = [0]
        for a in runningCosts:
            pre.append(pre[-1]+a)
        l = 0
        mx = 0
        sl = SortedList([(0,-1)])
        for i in range(n):
            sl.add((chargeTimes[i],i))
            while sl[-1][0] + (i-l+1)*(pre[i+1] - pre[l])> budget:
                sl.remove((chargeTimes[l],l))
                l +=1
            mx = max(i-l+1,mx)
        return mx
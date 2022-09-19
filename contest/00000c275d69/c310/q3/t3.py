from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        dic=defaultdict(int)
        ls =[]
        for a,b in intervals:
            heappush(ls,(a,1))
            heappush(ls,(b+1,-1))
        acc =0
        mx =0
        while ls:
            _,dif = heappop(ls)
            acc +=dif
            mx = max(mx,acc)
        return mx




re =Solution().minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]])
print(re)
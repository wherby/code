#https://leetcode.com/contest/biweekly-contest-64/problems/two-best-non-overlapping-events/
# remove limitation on two selections
from sortedcontainers import SortedDict,SortedList
class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        sl = SortedList([(0,0)])
        events.sort(key=lambda v : v[1])
        for s,e,v in events:
            idx = sl.bisect_right((s,0))
            value  = sl[idx-1][1]+ v 
            sl.add((e,value))
            while len(sl) > idx +1 and sl[idx][1] >= sl[idx+1][1]:
                sl.remove(sl[idx +1])
            print(sl)
        return sl[-1][1]
        


re = Solution().maxTwoEvents([[10,83,53],[63,87,45],[97,100,32],[51,61,16]])
print(re)
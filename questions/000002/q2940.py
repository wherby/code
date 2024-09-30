
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from sortedcontainers import SortedDict,SortedList

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ret = [-1]*n
        dic = defaultdict(list)
        sl = SortedList([])
        for i,(a,b) in enumerate(queries):
            a,b = min(a,b),max(a,b)
            if a == b:
                ret[i] = a 
            elif heights[a] < heights[b]:
                ret[i] = b 
            else:
                dic[b].append((heights[a],a,i))
        for i,a in enumerate(heights):
            while sl and sl[0][0] <a:
                b =sl[0]
                sl.remove(b)
                ret[b[2]] =i 
            for c in dic[i]:
                sl.add(c)
        return ret
    
re =Solution().leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]])
print(re)
            
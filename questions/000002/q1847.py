from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
from sortedcontainers import SortedDict,SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        ls = []
        for i,(p,s) in enumerate(queries):
            ls.append((s,p,i))
        ls.sort(reverse=True)
        sl = SortedList([])
        rooms.sort(key=lambda x: x[1])
        n = len(queries)
        res = [-1]*n
        for s,p,i in ls:
            while rooms and rooms[-1][1]>=s:
                sl.add(rooms[-1][0])
                rooms.pop()
            k = sl.bisect_left(p)
            ret = 10**10
            idx = -1
            if k >0 and len(sl):
                ret = min(ret, p-sl[k-1])
                idx = sl[k-1]
            if k < len(sl) and sl[k] - p < ret:
                idx =sl[k]
            res[i] = idx
        return res 


re = Solution().closestRoom(rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]])
print(re)


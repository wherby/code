from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        l,r = 0, min(len(tasks),len(workers))
        tasks.sort()
        workers.sort()

        def verify(mid):
            ws = workers[-mid:]
            ts = SortedList()
            for i in range(mid):
                ts.add(tasks[i])
            ps =pills
            for w in ws:
                if w < ts[0]:
                    if ps:
                        k = ts.bisect_right(w+strength)
                        if k>0:
                            ts.remove(ts[k-1])
                            ps -=1
                        else:
                            return False
                    else:
                        return False
                else:
                    ts.remove(ts[0])
            return True
        while l <r :
            mid = (l+r+1)>>1
            if verify(mid):
                l = mid 
            else:
                r= mid -1
        return l

from input import tasks,works,pills,strength
re = Solution().maxTaskAssign(tasks,works,pills,strength)
print(re)
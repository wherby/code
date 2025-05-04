from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        workers.sort()
        sl = SortedList([])
        for a in tasks:
            sl.add(a)
        cnt = 0 
        ws = SortedList(workers)
        for w in workers:
            k = sl.bisect_right(w)
            if k >0:
                sl.remove(sl[k-1])
                cnt +=1
                ws.remove(w)
        for w in ws[::-1]:
            k = sl.bisect_right(w)
            if k == 0:
                if pills:
                    k1 = sl.bisect_right(w+strength)
                    if k1>0:
                        sl.remove(sl[k1-1])
                        pills -=1
                        cnt +=1
            else:
                sl.remove(sl[k-1])
                cnt +=1
        return cnt
    
from input import tasks,works,pills,strength
re = Solution().maxTaskAssign(tasks,works,pills,strength)
print(re)
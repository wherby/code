from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        ls= [i for i in range(2002)]
        sl = SortedList(ls)
        tasks.sort(key = lambda x:x[1])
        for a,b,c in tasks:
            ia = sl.bisect_left(a-1)
            # if sl[ia] != a-1:
            #     ia +=1
            ib = sl.bisect_left(b-1)
            if sl[ib] != b-1:  ## ib could be next value 
                ib -=1
            #print(ia,ib)
            d = (b-a+1)-(ib-ia+1)
            res =[]
            while d < c:
                res.append(sl[ib])
                ib-=1
                d +=1
            for e in res:
                sl.remove(e)
        return 2002- len(sl)

re =Solution().findMinimumTime([[2000,2000,1]])             
#re = Solution().findMinimumTime([[2,3,1],[4,5,1],[1,5,2]])
#re = Solution().findMinimumTime([[1,10,7],[4,11,1],[3,19,7],[10,15,2]])
print(re)
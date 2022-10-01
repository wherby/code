# Using SortedList WIll timeout
from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        workers.sort()
        tasks.sort()
        l,r = 0,min(len(workers),len(tasks))
        def verify(mid):
            sw = workers[-mid:]
            st = tasks[:mid]
            ps =0
            wid = 0
            for w in sw:
                if w >= st[wid]:
                    wid +=1
                elif ps < pills and w + strength >=st[wid]:
                    ps +=1
                    wk = w +strength
                    k = bisect_right(st, wk)
                    st.pop(k-1)
                else:
                    return False
            return True
            
        while l<r:
            mid = (l+r+1)>>1
            if verify(mid):
                l = mid
            else:
                r = mid-1 
        return l
        
        

re =Solution().maxTaskAssign([35],[83,20,4,66],3,41)
print(re)
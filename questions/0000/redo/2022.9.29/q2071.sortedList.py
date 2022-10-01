# https://leetcode.com/submissions/detail/812407334/
from sortedcontainers import SortedDict,SortedList
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
            sl = SortedList(st)
            ps =0
            wid = 0
            for w in sw:
                if w >= sl[wid]:
                    wid +=1
                elif ps < pills and w + strength >=sl[wid]:
                    ps +=1
                    wk = w +strength
                    k = sl.bisect_right(wk)
                    sl.remove(sl[k-1])
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
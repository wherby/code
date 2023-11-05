
import heapq
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        q = []
        for a,b in classes:
            par =(a+1)*1.0/(b+1) -a*1.0/b
            heapq.heappush(q,(-par,a,b))
        while extraStudents >0:
            _,a,b = heapq.heappop(q)
            a+=1
            b+=1
            par =(a+1)*1.0/(b+1) -a*1.0/b
            heapq.heappush(q,(-par,a,b))
            extraStudents -=1
        res =0.0
        for p,a,b in q:
            res +=a*1.0 /b
        return res /len(q)

re = Solution().maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)
        
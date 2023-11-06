import math
class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        lo =1
        hi = 10**8
        def count(mid):
            sm = 0
            n = len(dist)
            for i in range(n-1):
                sm += math.ceil(dist[i] *1.0/mid)
            sm += dist[-1]  * 1.0/mid
            return sm
        while lo < hi:
            mid =(lo+hi) >>1
            if count(mid)>hour:
                lo=mid+1
            else:
                hi = mid
        if lo > 10**7:
            return -1
        return lo

re = Solution().minSpeedOnTime([1,1],1.0)
print(re)
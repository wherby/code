from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        l = 0
        r = sum(batteries) //n 
        m = len(batteries)
        batteries.sort()
        def isOk(mid):
            idx = bisect_right(batteries,mid)
            resN = n - (m -idx)
            #print(idx,mid,sum(batteries[:idx]),mid*resN )
            return sum(batteries[:idx]) >= mid*resN
        while l < r:
            mid = (l+r+1)>>1
            if isOk(mid):
                l = mid
            else:
                r =mid-1
        return l

re = Solution().maxRunTime(n = 2, batteries = [3,3,3])
print(re)
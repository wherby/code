

class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        l=1
        r = totalTrips*time[0]
        def check(mid):
            sm = 0 
            for t in time:
                sm += mid //t
            return sm 
        while l < r:
            mid = (l+r)>>1
            if check(mid) < totalTrips:
                l = mid +1
            else:
                r = mid
        return l

re =Solution().minimumTime(time = [5,10,10], totalTrips = 9)
print(re)

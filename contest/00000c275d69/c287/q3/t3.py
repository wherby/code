class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        def check(mid):
            cnt = 0
            for a in candies:
                cnt += a //mid
            return cnt >=k
        n = len(candies)
        candies.sort()

        l,r =0,candies[-1]
        while l < r:
            mid = (l+r+1)>>1
            if  check(mid):
                l = mid 
            else:
                r = mid-1
        return l

re = Solution().maximumCandies(candies = [1,2,3,4,10], k =5)
print(re)
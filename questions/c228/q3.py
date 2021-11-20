import math
class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        lo= 1
        hi = 10**9
        N = len(nums)

        def getNum(ls,k):
            cnt = 0
            for n in ls:
                cnt += math.ceil(n*1.0/k)
            return cnt -N
        while lo <hi:
            mid = (lo + hi)>>1
            if mid ==0:
                return 1
            if getNum(nums,mid) >maxOperations:
                lo = mid +1
            else:
                hi = mid
        return lo

re =Solution().minimumSize(nums = [1], maxOperations = 2)
print(re)

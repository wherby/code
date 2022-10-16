class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = nums[0]
        r = max(nums)
        sm = sum(nums)
        def verify(mid):
            acc =0 
            for i in range(n):
                acc += nums[i]
                if acc >mid*(i+1):
                    return False
            return True
        while l< r:
            mid = (l+r)>>1
            if not verify(mid):
               l=mid+1 
            else: 
                r =mid 
        return l




re =Solution().minimizeArrayValue([10,1])
print(re)
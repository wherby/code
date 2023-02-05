class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l,r = 0,max(nums)
        def verify(mid):
            cnt = 0
            lastUse = False
            for i,a in enumerate(nums):
                if a <= mid:
                    if lastUse == True:
                        lastUse = False
                    else:
                        cnt +=1
                        lastUse = True
                else:
                    lastUse = False
            return cnt >=k
        while l < r:
            mid = (l+r)>>1
            if not verify(mid):
                l = mid +1
            else:
                r = mid 
        return l

re = Solution().minCapability([24,1,55,46,4,61,21,52],3)
print(re)
# https://leetcode.cn/contest/weekly-contest-331/problems/house-robber-iv/
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
        
        
re =Solution().minCapability(nums = [2,3,5,9], k = 2)
print(re)
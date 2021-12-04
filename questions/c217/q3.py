class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        diff = [0]*200002
        for i in range(n//2):
            a,b = nums[i],nums[n-1-i]
            if a >b:
                a,b = b,a
            diff[2] +=2
            diff[a+1] -=1
            diff[a+b] -=1
            diff[a+b+1] +=1
            diff[limit +b+1] +=1
        ret = 2*200002
        y =0
        for x in range(2,200002):
            y += diff[x]
            ret = min(ret, y)
        return ret 

nums=[1,3,1,1,1,2,3,2,3,1,3,2,1,3]
limit=3
re = Solution().minMoves(nums,limit)
print(re)
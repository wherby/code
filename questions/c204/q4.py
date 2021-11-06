from functools  import lru_cache 
class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        @lru_cache(None) 
        def getInterleave(a,b):
            c= a+b
            re = 1
            a = min(a,b)
            for i in range(a):
                re = re * (c-i)//(i+1)
            return re
        def getRes(nums):
            if len(nums)<=1:
                return 1
            ls = [i for i in nums[1:] if i <nums[0]]
            rs = [i for i in nums[1:] if i > nums[0]]
            t = getInterleave(len(ls),len(rs))
            getRes(ls)
            getRes(rs)
            res.append(t)
        getRes(nums)
        #print(res)
        re = 1
        mod = 10**9+7
        for i in res:
            re = i*re %mod
        return re-1
            



re= Solution().numOfWays(nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18])
print(re)
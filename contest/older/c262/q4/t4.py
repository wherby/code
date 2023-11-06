import functools


class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        half = n//2
        msm = sum(map(lambda x: abs(x),nums))
        sm = sum(nums)
        print(nums,half,msm)
        mxV =[msm]
        @functools.lru_cache(None) 
        def dfs(v,index, cnt):
            if(mxV[0] ==0):
                return
            if cnt == half:
                t1 = sm-v 
                v1 = abs(t1 - v)
                mxV[0] = min(mxV[0],v1)
                #print(v1)
                return
            for i in range(index,n):
                dfs(v + nums[index],index +1,cnt +1)
                dfs(v,index+1,cnt)
        dfs(0,0,0)
        #print(mxV[0])
        return mxV[0]
    
re = Solution().minimumDifference([-88824,12448,-40806,-34141,-32662,-90262,19500,71449,35571,87200,55623,-67359,47753,-33611,82685,-8845,-66409,51305])
print(re)


        
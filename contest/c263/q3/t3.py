class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = 0
        for n in nums:
            target = target | n
        
        n = len(nums)
        res =[]
        def dpfs(idx,acc,target,ls):
            #print(idx,acc,ls)
            if acc ==target:
                #print(ls, (len(nums) - idx))
                res.append(1 * 2**(len(nums) - idx) )
                return
            if idx >= len(nums):
                return

            dpfs(idx +1,acc |nums[idx],target,ls+[nums[idx]])
            dpfs(idx+1, acc,target,ls)
        dpfs(0,0,target,[])
        #print(res,target)
        return(sum(res))
nums =  [2,2,2]
re = Solution().countMaxOrSubsets(nums)
print(re)

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        acc =0
        lst =0
        nums.append(1)
        for a in nums:
            if a ==0:
                lst +=1
            else:
                acc += lst*(lst+1)//2
                lst =0
        return acc





re =Solution().zeroFilledSubarray(nums = [0,0,0,2,0,0])
print(re)
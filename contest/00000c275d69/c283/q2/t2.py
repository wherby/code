
from bisect import bisect_right
class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        t = bisect_right(nums,k)
        dic ={}
        for a in nums:
            dic[a] =1
        sm = k*(k+1)//2 - sum(nums[:t])
        idx = 0
        for i in range(k+1,k+len(nums) +2):
            if idx == t:
                return sm
            if i not in dic:
                sm +=i
                idx  +=1

re =Solution().minimalKSum(nums = [1,4,25,10,25], k = 2)
print(re)
        
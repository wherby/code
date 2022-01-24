from collections import defaultdict
class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = defaultdict(int)
        for a in nums:
            dic[a] +=1
        n = len(nums)
        res=[]
        for i in range(n):
            if dic[nums[i]] ==1 and dic[nums[i]-1] ==0 and dic[nums[i]+1] ==0:
                res.append(nums[i])
        return res

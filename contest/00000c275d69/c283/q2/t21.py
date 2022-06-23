class Solution(object):
    def minimalKSum(self, nums, k):
        dic ={}
        for a in nums:
            dic[a] =1
        sm = 0
        idx =1
        for i in range(1,k+len(nums) +1):
            if idx ==k :
                return sm
            if i not in dic:
                sm +=i
                idx +=1
from collections import Counter
class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        cnt =0
        n = len(nums)
        dic = {}
        for i in range(n):
            acc =0
            ls =""
            for j in range(i,n):
                if nums[j]%p ==0:
                    acc +=1
                    if acc >k:
                        break
                cnt +=1
                ls +=str(nums[j]) + "*"
                dic[ls]=1
        return len(dic)
                
        
        
        
re = Solution().countDistinct(nums = [2,3,3,2,2], k = 2, p = 2)
#re = Solution().countDistinct(nums = [1,2,3,4], k = 4, p = 1)
print(re)
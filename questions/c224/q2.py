from collections import defaultdict
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                t = nums[i]* nums[j]
                dic[t].append([nums[i],nums[j]])
        cnt =0
        for k,v in dic.items():
            m = len(v)
            if m >=2:
                cnt += m*(m-1) //2 *8
        return cnt

nums = [2,3,4,6,8,12]
re = Solution().tupleSameProduct(nums)
print(re)
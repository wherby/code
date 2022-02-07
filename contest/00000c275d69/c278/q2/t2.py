


class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ls = [0]*(n+1)
        ls1 = [0]*(n+2)
        sm = 0
        for i,a in enumerate(nums):
            if a ==0:
                ls[i+1]= ls[i]+1
            else:
                ls[i+1]= ls[i]
            if nums[n-i-1] ==1:
                ls1[n-i-1] =ls1[n-i] +1
            else:
                ls1[n-i-1] =ls1[n-i]
        ls2 =[0]*(n+1)
        for i in range(n+1):
            ls2[i] = ls[i] + ls1[i]
        mx = max(ls2)
        res =[]
        for i in range(n+1):
            if mx == ls2[i]:
                res.append(i)
        return res


re = Solution().maxScoreIndices(nums = [0,0,1,0])
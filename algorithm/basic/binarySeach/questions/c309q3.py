# https://leetcode.cn/contest/weekly-contest-309/problems/longest-nice-subarray/
class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ls = [[0]*32 for _ in range(n+1)]
        for i in range(n):
            for j in range(32):
                if (1<<j) & nums[i]:
                    ls[i+1][j] =ls[i][j] +1
                else:
                    ls[i+1][j] = ls[i][j]
        l,r = 2,n+1 # return l-1 , l,r need to add 1
        def verify(mid):
            for i in range(n-mid+1):
                isGood = True
                for j in range(32):
                    if ls[i+mid][j] -ls[i][j] >1:
                        isGood = False
                        break # if not break, will timeout
                if isGood ==True:
                    return True
            return False
        while l <r:
            mid = (l+r)>>1
            if  verify(mid):
                l = mid+1
            else:
                r = mid 
        return l-1
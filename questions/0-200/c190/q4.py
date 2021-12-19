class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m,n = len(nums1),len(nums2)
        dp = [[-10**20]*(n+1) for _ in range(m+1)]
        for x in range(n):
            dp[1][x+1] =max(dp[1][x], nums1[0]* nums2[x]) 
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1]= max(dp[i+1][j+1],nums1[i]*nums2[j] + dp[i][j],nums1[i] *nums2[j],dp[i][j+1],dp[i+1][j])
        #print(dp)
        return dp[m][n]

re = Solution().maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7])
print(re)
class Solution(object):
    def kthLargestValue(self, matrix, k):
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        ans =[]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j] ^ dp[i][j-1] ^ dp[i-1][j-1] ^ matrix[i-1][j-1]
                ans.append(dp[i][j])
        ans =sorted(ans,reverse=True)
        return ans[k-1]

re =Solution().kthLargestValue([[8,10,5,8,5,7,6,0,1,4,10,6,4,3,6,8,7,9,4,2]],2)
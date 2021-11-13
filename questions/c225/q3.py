class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        pre  = [[matrix[0][0]]*n for i in range(m)]
        for i in range(1,n):
            pre[0][i] = pre[0][i-1] ^ matrix[0][i]
        for j in range(1,m):
            pre[j][0] = pre[j-1][0] ^ matrix[j][0]
        for i in range(1,m):
            for j in range(1,n):
                pre[i][j] = pre[i][j-1] ^ pre[i-1][j] ^pre[i-1][j-1]^matrix[i][j]
        left,right= 0,100000000
        def count(mid):
            cnt =0
            for i in range(m):
                for j in range(n):
                    if pre[i][j]>=mid:
                        cnt +=1
            return cnt
        while left<right:
            mid = right -(right-left) //2
            num = count(mid)
            if num <k:
                right =mid-1
            else:
                left = mid
        return left
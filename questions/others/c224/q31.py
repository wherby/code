class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        mx = 0
        for i in range(m):
            ls = []
            for j in range(n):
                t =i
                while t <m and matrix[t][j] ==1:
                    t +=1
                ls.append(t-i)
            ls = sorted(ls,key= lambda x: -x)
            for  k in range(n):
                t = (k+1)* ls[k]
                mx =max(t,mx)
            if mx > (m-i)*n:
                break
        return mx
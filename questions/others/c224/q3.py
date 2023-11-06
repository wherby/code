#
class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        mx = 0
        ls =[0]*n
        for i in range(m):
            for j in range(n):
                t =i
                if(ls[j])>0:         #优化
                    ls[j] = ls[j]-1  # 
                else:
                    while t <m and matrix[t][j] ==1:
                        t +=1
                    ls[j] =(t-i)
            lsT = sorted(ls,key= lambda x: -x) # 如果保留上次结果就需要换个变量
            for  k in range(n):
                t = (k+1)* lsT[k]
                mx =max(t,mx)
            if mx > (m-i)*n:
                break
        return mx

matrix = [[0,0,1],[1,1,1],[1,0,1]]
re =Solution().largestSubmatrix(matrix)
print(re)
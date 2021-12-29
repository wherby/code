class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(mat),len(mat[0])
        def sortls(x1,y1):
            x,y = x1,y1
            ls =[]
            while x >=0 and x <m and y >=0 and y <n:
                ls.append(mat[x][y])
                x +=1
                y+=1
            ls.sort()
            x,y = x1,y1
            idx =0
            while x >=0 and x <m and y >=0 and y <n :
                mat[x][y] = ls[idx]
                idx +=1
                x +=1
                y +=1
        for i in range(n):
            x,y = 0,i
            sortls(x,y)
        for i in range(m):
            x,y = i,0
            sortls(x,y)
        return mat

re = Solution().diagonalSort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]])
print(re)
import heapq
class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m,n= len(grid),len(grid[0])
        pre1 = [[0]*n for _ in range(m)]
        pre2 = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                pre1[i][j]= grid[i][j] + (pre1[i-1][j-1] if i-1>=0 and j-1>=0 else 0)
        for i in range(m):
            for j in range(n-1,-1,-1):
                pre2[i][j] = grid[i][j] + (pre2[i-1][j+1] if i-1 >=0 and j+1<n else 0)

        st =[]
        for i in range(m):
            for j in range(n):
                R = min(i,j, m-1-i,n-1-j)
                heapq.heappush(st,-grid[i][j])
                for  r in range(1,R+1):
                    sm = 0
                    x1,y1,x2,y2 = i-r,j,i,j+r
                    sm += pre1[x2][y2] -(pre1[x1-1][y1-1] if x1-1>=0 and y1-1>=0 else 0)
                    x1,y1,x2,y2 = i,j-r,i+r,j
                    sm += pre1[x2][y2] - (pre1[x1-1][y1-1] if x1-1>=0 and y1-1>=0 else 0)
                    x1,y1,x2,y2 = i-r,j,i,j-r
                    sm += pre2[x2-1][y2+1] - pre2[x1][y1]
                    x1,y1,x2,y2 = i, j+r,i+r,j
                    sm += pre2[x2-1][y2+1] - pre2[x1][y1]
                    heapq.heappush(st,-sm)
        re = []
        while st and len(re)<3:
            k = heapq.heappop(st)
            re.append(-k)
            if len(re)>1 and re[-1] == re[-2]:
                re.pop()
        return re

#re = Solution().getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]])
re = Solution().getBiggestThree([[20,17,9,13,5,2,9,1,5],[14,9,9,9,16,18,3,4,12],[18,15,10,20,19,20,15,12,11],[19,16,19,18,8,13,15,14,11],[4,19,5,2,19,17,7,2,2]])
print(re)
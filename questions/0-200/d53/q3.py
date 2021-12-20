import heapq
class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m,n= len(grid),len(grid[0])
        st =[]
        for i in range(m):
            for j in range(n):
                R = min(i,j, m-1-i,n-1-j)
                heapq.heappush(st,-grid[i][j])
                for  r in range(1,R+1):
                    a,b = i-r,j
                    sm = 0
                    for _ in range(r):
                        a +=1
                        b-=1
                        sm += grid[a][b]
                    for _ in range(r):
                        a +=1
                        b +=1
                        sm += grid[a][b]
                    for _ in range(r):
                        a -=1
                        b +=1
                        sm += grid[a][b]
                    for _ in range(r):
                        a -=1
                        b-=1
                        sm += grid[a][b]
                    heapq.heappush(st,-sm)
        re = []
        while st and len(re)<3:
            k = heapq.heappop(st)
            re.append(-k)
            if len(re)>1 and re[-1] == re[-2]:
                re.pop()
        return re

re = Solution().getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]])
print(re)
import heapq
class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        dirs = [[-1,0],[0,-1],[0,1],[1,0]]
        m,n = len(grid),len(grid[0])
        visited = [[0]*n for _ in range(m)]
        visited[start[0]][start[1]]=1
        st =[start]
        res =[]
        while k and st:
            tmp=[]
            valid=[]

            for x,y in st:
                for dir in dirs:
                    #print(dir)
                    x1 = x + dir[0]
                    y1 = y + dir[1]
                    if x1 >=0 and x1 <m and y1>=0 and y1<n and grid[x][y] != 0 and visited[x1][y1] ==0 :
                        #print(x1,y1,dir,x,y)
                        visited[x1][y1] = 1
                        tmp.append([x1,y1])
                if grid[x][y] >=pricing[0] and grid[x][y] <= pricing[1]:
                    heapq.heappush(valid,(grid[x][y],x,y))
            st = tmp
            #print(valid)
            while valid and k:
                k -=1
                v = heapq.heappop(valid)
                res.append([v[1],v[2]])
            #print(tmp,k,res)
        return res

re = Solution().highestRankedKItems(grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3)
print(re)


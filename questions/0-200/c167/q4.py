class Solution(object):
    def shortestPath(self, grid, k):
        m,n = len(grid),len(grid[0])
        visitedLs=[]
        for _ in range(k+1):
            visited = [[10**8] *n  for _ in range(m)]
            visitedLs.append(visited)
        visitedLs[k][0][0] =0 
        st = [(0,0,k,0)]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while st:
            x,y,kth,cost = st.pop(0)
            
            for d in dirs:
                x1 = x + d[0]
                y1 = y + d[1]
                if x1 >=0 and x1<m and y1 >=0 and y1<n:
                    if grid[x1][y1] == 1 and kth >0 and visitedLs[kth-1][x1][y1] > cost+1:
                        st.append((x1,y1,kth-1,cost+1))
                        visitedLs[kth-1][x1][y1] = cost +1
                    if grid[x1][y1] ==0 and visitedLs[kth][x1][y1] > cost+1:
                        st.append((x1,y1,kth,cost +1))
                        visitedLs[kth][x1][y1] = cost +1
        re = []
        for i in range(k+1):
            re.append(visitedLs[i][m-1][n-1])
        mn = min(re)
        if mn ==10**8:
            return -1
        return mn

re = Solution().shortestPath(grid = [[0]], 
k = 1)
print(re)

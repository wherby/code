class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        if grid[0][0] != 0 :
            return -1
        visited =[[0]*n for i in range(m)]
        st =[(0,0,1)]
        visited[0][0] =1
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        while st:
            x,y,c = st.pop(0)
            if x == m-1 and y == n-1:
                return c
            for d in dirs:
                x1,y1 = x + d[0],y + d[1]
                if x1>=0 and x1 <m and y1>=0 and y1 <n  and visited[x1][y1] == 0 and grid[x1][y1] ==0:
                    visited[x1][y1] = 1
                    st.append((x1,y1,c+1))
        #print(visited)
        return -1

re = Solution().shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]])
print(re)
            
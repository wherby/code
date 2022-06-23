class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(heights),len(heights[0])
        visit1 = [[0]*n for _ in range(m)]
        visit2=[[0]*n for _ in range(m)]
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        seed1 = []
        seed2 = []
        
        for i in range(n):
            seed1.append([0,i])
            seed2.append([m-1,i])
        for i in range(m):
            seed1.append([i,0])
            seed2.append([i,n-1])
        def visit(seed,visit):
            while seed:
                #print(seed)
                x,y = seed.pop()
                if visit[x][y]==1: continue
                visit[x][y] = 1
                for dx,dy in dirs:
                    nx,ny = dx + x ,y+dy
                    if 0<=nx and nx< m and ny>=0 and ny < n and visit[nx][ny] ==0 and heights[x][y]<= heights[nx][ny]:
                        seed.append([nx,ny])
        visit(seed1,visit1)
        visit(seed2,visit2)
        ret =[]
        for i in range(m):
            for j in range(n):
                if visit1[i][j] and visit2[i][j]:
                    ret.append([i,j])
        return ret
                    
                
                
        
        

re = Solution().pacificAtlantic(heights =[[1,1],[1,1],[1,1]])
print(re)
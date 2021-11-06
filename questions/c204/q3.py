class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        def isValid(a,b):
            if a >=0 and a<m and b >=0 and b < n:
                return True
            return False
        g =[]
        for i in range(m):
            t = [[] for j in range(n)]
            g.append(t)
        dir =[[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    for d in dir:
                        x1 = i +d[0]
                        y1 = j + d[1]
                        if isValid(x1,y1):
                            if grid[x1][y1] ==1:
                                g[i][j].append([x1,y1])
        visited =[[-1]*n for i in range(m)]
        cand = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cand.append([i,j])
                    visited[i][j] = 0
        def bfs(start):
            q =[start]
            cnt = 0
            visited[start[0]][start[1]] =1
            while q:
                t =q.pop(0)
                cnt +=1
                a,b = t[0],t[1]
                
                for x in g[a][b]:
                    if visited[x[0]][x[1]] == 0:
                        q.append(x)
                        visited[x[0]][x[1]] =1
            return cnt
        m = bfs(cand[0])
        #print(m,len(cand))
        if m != len(cand):
            return 0
        if len(cand) <2:
            return len(cand)
        for c in cand:
            for c1 in cand:
                visited[c1[0]][c1[1]] =0
            visited[c[0]][c[1]] =1
            start= cand[0]
            if start[0] == c[0] and start[1]  == c[1]:
                start = cand[1]
            m = bfs(start)
            if m != len(cand) -1:
                return 1
        return 2
            


grid = [[1,1,0,1,1],[1,1,1,1,1], [1,1,0,1,1], [1,1,1,1,1]]

re =Solution().minDays(grid)
print(re)
from collections import defaultdict
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m = len(grid1)
        n = len(grid1[0])
        def isValid(x,y):
            return x >=0 and x <m and y >=0 and y<n
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        visted = [[0]*n for _ in range(m)]
        
        def dfs(g, x,y,k):
            if visted[x][y] ==1:
                return
            visted[x][y] =1
            res = []
            if g[x][y] == 1:
                g[x][y] =k
                for a,b in dirs:
                    x1 = x +a
                    y1 = y +b
                    if isValid(x1,y1) and visted[x1][y1] ==0:
                        dfs(g,x1,y1,k)
                return res
            else:
                return []
        
        for i in range(m):
            for j in range(n):
                k =i*m+j +10
                dfs(grid1,i,j,k)
                
        visted = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                k =i*n+j +10
                dfs(grid2,i,j,k)
        res2=defaultdict(list)
        for i in range(m):
            for j in range(n):        
                t = grid2[i][j]
                if t >0:
                    res2[t].append([i,j])
        ret =0
        #print(res2,len(res2))
        for k,v in res2.items():
            res =[]
            for x,y in v:
                t = grid1[x][y]
                if t == 0:
                    break
                res.append(t)
            if len(set(res)) ==1 and len(res) == len(v):
                ret +=1
        return ret

grid1 = [[1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1],[1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1],[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1],[0,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1],[1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1],[0,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,0,1],[1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1],[1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0],[0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0],[0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],[1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,1],[1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,1]]


grid2 =[[1,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1],[0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1],[1,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1],[0,1,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,1,0,0],[1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0],[0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,1,0,1,0,0],[1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1],[0,1,1,0,0,1,1,0,0,0,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0],[0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0],[1,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0],[1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,1,0],[0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1],[1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,0,1,1,1],[1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,1]]


re =Solution().countSubIslands(grid1,grid2)
print(re)
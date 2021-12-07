
class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        visited = [[0]*n for _ in range(m)]
        def valid(x,y):
            if x>=0 and x <m and y >= 0 and y <n:
                return True
            return False
        cands =[]
        def dfs(x,y,c,c2):
            if not valid(x,y):
                return
            if visited[x][y] ==0:
                visited[x][y] =1
                if grid[x][y] == c:
                    cands.append((x,y))
                    dfs(x+1,y,c,c2)
                    dfs(x-1,y,c,c2)
                    dfs(x,y+1,c,c2)
                    dfs(x,y-1,c,c2)
        dfs(row,col, grid[row][col],color)
        res =[]
        c = grid[row][col]
        for x,y in cands:
            if x ==0 or y ==0 or x ==m-1 or y == n-1:
                res.append((x,y))
                continue
            if grid[x-1][y] == c and grid[x+1][y] == c and grid[x][y+1] ==c and grid[x][y-1] == c:
                continue
            res.append((x,y))
        for x,y in res:
            grid[x][y] = color
        return grid


re = Solution().colorBorder(grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 2, color = 2)
print(re)
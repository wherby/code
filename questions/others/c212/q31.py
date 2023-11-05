import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows,cols = len(heights),len(heights[0])
        hp = [(0,rows-1,cols-1)]
        visited = [[0]*cols for _ in range(rows)]
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        
        while hp:
            effort, x,y = heapq.heappop(hp)
            if visited[x][y]:
                continue
            if x ==0 and y ==0:
                return effort
            visited[x][y] =1
            for dx,dy in dirs:
                nx,ny = x + dx,y + dy
                if 0<=nx <rows and 0<= ny<cols and not visited[nx][ny]:
                    heapq.heappush(hp,(max(effort,abs(heights[nx][ny]-heights[x][y])),nx,ny))

re = Solution().minimumEffortPath(heights = [[10,8],[10,8],[1,2],[10,3],[1,3],[6,3],[5,2]])
print(re)

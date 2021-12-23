from collections import deque
class Solution(object):
    def shortestPath(self, grid, k):
        m,n = len(grid),len(grid[0])
        if m ==1 and n ==1:
            return 0

        if k > m+n -3:
            return m +n -2
        q = deque([(0,0,k,0)])
        visited =set((0,0,k))
        while q:
            x,y,z,cost = q.popleft()
            nbrs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            if x == m-1 and y ==n-1:
                return cost
            for nx, ny in nbrs:
                temp = z
                if 0 <= nx < m and 0 <= ny < n:
                    temp -= grid[nx][ny]
                    if (not (nx, ny, temp) in visited) and temp >= 0:
                        visited.add((nx, ny, temp))
                        q.append((nx, ny, temp,cost +1))
        return -1

re = Solution().shortestPath(grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1)
print(re)
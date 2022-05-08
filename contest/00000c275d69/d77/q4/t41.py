from collections import deque
import heapq
class Solution(object):
    def maximumMinutes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dir =[[1,0],[-1,0],[0,1],[0,-1]]
        m,n = len(grid),len(grid[0])
        st =deque([])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    st.append([i,j,0])
        mx =1000000
        mp =[[mx]*n for _ in range(m)]
        while st:
            x,y,t = st.popleft()
            if mp[x][y] ==mx:
                mp[x][y] =t
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if nx>=0 and nx <m and ny>=0 and ny <n and grid[nx][ny] !=2 and mp[nx][ny] ==mx:
                    st.append([nx,ny,t+1])
        st = deque([(mp[0][0]-1,0,0,0)])
        mp2 =[[-1]*n for _ in range(m)]
        ans = -1
        #print(mp)
        while st:
            delt,x,y,t = st.popleft()
            if delt <=mp2[x][y]:continue
            mp2[x][y] =delt 
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if nx>=0 and nx <m and ny>=0 and ny <n and grid[nx][ny] !=2 :
                    if nx ==m-1 and ny==n-1 and mp[nx][ny]>= t+1:
                        mp2[nx][ny] = max(mp2[nx][ny],min(mp[nx][ny] -1- t,delt))
                    tdt = mp[nx][ny] -1- t-1
                    tdt = min(delt,tdt)
                    if tdt >=0:
                        st.append((tdt,nx,ny,t+1))
        #print(mp2)
        return mp2[m-1][n-1] if mp2[m-1][n-1] < 20000 else 10**9
    
    
# #re = Solution().maximumMinutes(grid = [[0,2,0,0,1],
#                                        [0,2,0,2,2],
#                                        [0,2,0,0,0],
#                                        [0,0,2,2,0],
#                                        [0,0,0,0,0]])
#re = Solution().maximumMinutes(grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]])
#re = Solution().maximumMinutes([[0,2,0,0,0,0,0,0,0,2,0,2,0,2,2,0,2,0,0,0,0,0],[0,0,0,2,2,2,0,2,0,0,0,0,0,0,0,0,0,0,2,2,2,2],[0,2,2,2,2,2,2,2,2,0,2,2,2,0,2,2,2,0,0,2,0,2],[0,0,2,0,0,0,2,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0],[2,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,2,0],[0,0,2,0,2,0,2,2,0,0,0,2,2,2,2,0,2,2,0,0,2,0],[2,2,2,0,2,2,2,2,2,2,0,0,0,0,2,0,0,2,2,0,2,0],[0,0,0,0,0,0,0,0,0,2,0,2,0,2,2,2,2,2,2,0,2,0],[2,0,2,0,2,0,2,0,2,2,0,2,0,0,0,0,2,0,2,0,2,2],[0,0,2,0,2,0,2,0,2,2,0,2,2,0,2,0,0,0,2,2,2,2],[0,2,2,0,2,0,2,0,2,1,0,0,2,2,2,0,2,0,0,2,0,0],[0,2,2,0,2,2,2,0,2,2,2,0,0,0,2,0,2,2,0,0,0,2],[0,2,2,0,2,0,0,0,0,0,2,2,0,2,2,2,1,2,2,0,2,1],[0,2,2,0,2,2,2,0,2,0,2,2,0,0,0,0,2,2,0,0,0,2],[0,2,0,0,2,0,0,0,2,0,2,0,0,2,0,2,2,0,0,2,0,0],[2,2,2,0,2,2,0,2,2,0,2,2,0,2,2,2,2,2,0,2,2,0],[0,0,0,0,2,2,0,2,0,0,2,2,0,0,0,0,0,2,0,2,0,0]])
re = Solution().maximumMinutes([[0,0,0,0,0],
                                [0,2,0,2,0],
                                [0,2,0,2,0],
                                [0,2,1,2,0],
                                [0,2,2,2,0],
                                [0,0,0,0,0]])
#re = Solution().maximumMinutes([[0,0,0],[2,2,0],[1,2,0]])
re =Solution().maximumMinutes([[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]])
print(re)
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
        st = [(-mp[0][0]+1,0,0,0)]
        mp2=[[mx]*n for _ in range(m)]
        ans =-1
        print(mp)
        while st:
            dt,x,y,t = heapq.heappop(st)
            # if len(st)>100:
            #     break
            print(dt,x,y,t,mp[x][y],len(st),mx)
            #if mp2[x][y] != mx:continue
            mp2[x][y] ==t
            if x == m-1 and y == n-1 :
                if dt < -20000:
                    ans = 10**9
                print("cc",dt)
                ans =max( -dt,ans) 
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if nx>=0 and nx <m and ny>=0 and ny <n and grid[nx][ny] !=2 and mp2[nx][ny] ==mx:
                    
                    if nx == m-1 and ny ==n-1 and t+1 == mp[nx][ny]:
                        #print("bb")
                        ans =max(ans,0)
                    ddt =t+1-mp[nx][ny]+1
                    ddt= max(dt,ddt)
                    
                    if ddt >0:continue
                    heapq.heappush(st,(ddt,nx,ny,t+1))
                    #mp2[nx][ny] =1
                    
        return ans
    
    
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
print(re)
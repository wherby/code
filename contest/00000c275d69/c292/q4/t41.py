from collections import defaultdict,deque
class Solution:
    def hasValidPath(self, grid) -> bool:
        m,n = len(grid),len(grid[0])
        if grid[0][0] == ")":
            return False
        st = deque([(0,0,1)])
        dic ={}
        dirs = [[1,0],[0,1]]
        mx = (m+n+4) //2
        dp =[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = [0]*mx
        while st:
            x,y,cnt =st.popleft()
            if x == m-1 and y == n-1 and cnt ==0:
                return True
            dic[(x,y,cnt)] =1
            for dx,dy in dirs:
                nx,ny = x+ dx ,y +dy
                if  0<=nx <m and 0<=ny<n:
                    if grid[nx][ny] =="(":
                        ncnt = cnt +1
                        if ncnt >= m+n -nx-ny:
                            continue
                        if dp[nx][ny][ncnt]==0:
                            st.append((nx,ny,ncnt))
                            dp[nx][ny][ncnt]=1
                    else:
                        ncnt = cnt -1
                        if ncnt >=0:
                            if dp[nx][ny][ncnt]==0:
                                st.append((nx,ny,ncnt))
                                dp[nx][ny][ncnt]=1
        return False
    
re  = Solution().hasValidPath([["(",")"],["(",")"]])
print(re)

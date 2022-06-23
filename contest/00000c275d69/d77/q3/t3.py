class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        dir =[[1,0],[-1,0],[0,1],[0,-1]]
        grid =[[0]*n for _ in range(m)]
        st= []
        for x,y in guards:
            grid[x][y]=2
            for dx,dy in dir:
                st.append((x,y,dx,dy))
        for x,y in walls:
            grid[x][y] =2
        while st:
            x,y,dx,dy = st.pop()
            if x+dx >=0 and x +dx <m and y+dy >=0 and dy+y <n :
                nx=x+dx
                ny = y+dy
                if grid[nx][ny] != 2:
                    grid[nx][ny] =1
                    st.append((nx,ny,dx,dy))
            else:
                continue
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==0:
                    cnt +=1
        return cnt
        
        
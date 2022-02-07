class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(isWater),len(isWater[0])
        g = [[0] * n for _ in range(m)]
        visited =[[0]*n for _ in range(m)]
        st =[]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] ==1:
                    st.append([i,j])
        idx =0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while st:
            tmp =[]
            for x,y in st:
                if visited[x][y] :continue 
                visited[x][y] = 1
                g[x][y] = idx
                for dir in dirs:
                    x1,y1 = x + dir[0],y +dir[1]
                    if x1 >=0 and x1 <m and y1 >=0 and y1<n and visited[x1][y1] ==0:
                        tmp.append([x1,y1])
            st = tmp
            idx +=1
        return g

re =Solution().highestPeak([[0,0,1],[1,0,0],[0,0,0]])
print(re)

        
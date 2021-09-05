class Solution:
    def findFarmland(self, land):
        re = []
        m = len(land)
        if m ==0:
            return []
        n = len(land[0])
        visited = {}
        def dfs(i,j):
            st=[(i,j)]
            mxi=i
            mxj =j
            while len(st) != 0:
                i,j = st.pop()
                mxi = max(mxi, i)
                mxj = max(mxj,j)
                visited[(i,j)]=1
                if i + 1 < m and land[i+1][j] ==1 and (i+1,j) not in visited:
                    st.append((i+1,j))
                if j + 1 < n and land[i][j+1] ==1 and (i,j+1) not in visited:
                    st.append((i,j+1)) 
            return [mxi,mxj]
               
        for i in range(m):
            for j in range(n):
                if land[i][j] ==1 and (i,j) not in visited:
                    start = [i,j]
                    end= dfs(i,j)
                    re.append([start[0],start[1],end[0],end[1]])
        return re
        


land = [[1,0,0],[0,1,1],[0,1,1]]
re= Solution().findFarmland(land)
print(re)

land = [[1,1],[1,1]]
re= Solution().findFarmland(land)
print(re)

land = [[0]]
re= Solution().findFarmland(land)
print(re)
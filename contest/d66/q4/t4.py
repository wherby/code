class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dpl = [[0]*n for _ in range(m)]
        dpr = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==0:
                    dpl[i][j] =0
                else:
                    if j ==0:
                        dpl[i][j] =1
                    else:
                        dpl[i][j] = dpl[i][j-1] + grid[i][j]
        for i in range(m):
            for j in range(n-1,-1,-1):
                if grid[i][j] ==0:
                    dpr[i][j] =0
                else:
                    if j == n-1:
                        dpr[i][j] =1
                    else:
                        dpr[i][j] = dpr[i][j+1] + grid[i][j]
        cnt =0
        mxSize =list(grid[0])
        def checkM(j,z):
            return min(mxSize[j],z-1)
        #print(dpl)
        #print(dpr)
        for i in range(1,m):
            for j in range(1,n-1):
                z = min(dpl[i][j],dpr[i][j])
                k = max( checkM(j,z),0)
                cnt +=k
                if grid[i][j] ==0:
                    mxSize[j] =0
                else:
                    mxSize[j] =k+1
            #print(mxSize,cnt,"ccc")
        #print(cnt)
        mxSize = list(grid[m-1])
        for i in range(m-2,-1,-1):
            for j in range(1,n-1):
                #print(i,j)
                z = min(dpl[i][j],dpr[i][j])
                k = max(checkM(j,z),0)
                cnt += k
                #print(k)
                if grid[i][j] ==0:
                    mxSize[j] =0
                else:
                    mxSize[j] = k+1
        return cnt

re = Solution().countPyramids(grid = [[0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,1,0,0],[1,1,1,1,1,1,1]])
print(re)
#[[0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,0,0],
# [1,1,1,1,1,1,1]]
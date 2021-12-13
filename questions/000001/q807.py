class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        mls,nls = [0]*m,[0]*n
        for i in range(m):
            for j in range(n):
                mls[i] = max(mls[i],grid[i][j])
                nls[j] = max(nls[j],grid[i][j])
        res = [[0]*n for _ in range(m)]
        cnt =0
        for i in range(n):
            for j in range(m):
                res[i][j] = min(mls[i],nls[j])
                cnt += res[i][j] -grid[i][j]
        return cnt
        


re = Solution().maxIncreaseKeepingSkyline(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
print(re)
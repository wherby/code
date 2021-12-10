class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        l = 0
        r =10**6
        m = len(heights)
        n = len(heights[0])
        def check(mid):
            visited=[[0]*n for _ in range(m)]
            result = False
            def dfs(x,y,k1):
                nonlocal result
                if x >=0 and x < m  and y >=0 and y <n  and visited[x][y] ==0 and abs(heights[x][y] - k1) <=mid:
                    visited[x][y] =1
                    if x ==m-1 and y == n-1:
                        result = True
                        return
                    k2 = heights[x][y]
                    dfs(x-1,y,k2)
                    dfs(x+1,y,k2)
                    dfs(x,y+1,k2)
                    dfs(x,y-1,k2)
            dfs(0,0,heights[0][0])
            #print(visited,mid)
            return result
        while l <r:
            mid =(l+r)>>1
            if check(mid)== True:
                r =mid
            else:
                l = mid+1
        return l

re = Solution().minimumEffortPath(heights = [[10,8],[10,8],[1,2],[10,3],[1,3],[6,3],[5,2]])
print(re)
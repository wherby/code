#https://leetcode.com/articles/cherry-pickup/

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        mem = [[[None] * n for _1 in range(n)] for _2 in range(n)]

        def dp(r1,c1,c2):
            r2 = r1 +c1 -c2
            if n== r1 or n == c1 or n ==r2 or n ==c2 or grid[r1][c1] ==-1  or grid[r2][c2] ==-1:
                return float('-inf')
            elif r1==c1 == n-1:
                return grid[r1][c1]
            elif mem[r1][c1][r2] is not None:
                return mem[r1][c1][r2]
            else:
                ans = grid[r1][c1] + (c1 != c2) *grid[r2][c2]
                ans += max(dp(r1,c1+1,c2+1),dp(r1+1,c1,c2+1),dp(r1,c1+1,c2),dp(r1+1,c1,c2))
            mem[r1][c1][c2] = ans
            return ans
        return max(0,dp(0,0,0))




s = Solution()
grid =[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
print s.cherryPickup(grid)
# https://leetcode.cn/problems/cherry-pickup/
# https://leetcode.cn/problems/cherry-pickup/solution/zhai-ying-tao-by-leetcode-solution-1h3k/
#一个N x N的网格(grid) 代表了一块樱桃地，每个格子由以下三种数字的一种来表示：

#0 表示这个格子是空的，所以你可以穿过它。
#1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
#-1 表示这个格子里有荆棘，挡着你的路。
#你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：

#从位置 (0, 0) 出发，最后到达 (N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；
#当到达 (N-1, N-1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
#当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；
#如果在 (0, 0) 和 (N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dp = [[[-10**10]*n  for _ in range(n)] for _ in range(2*n-1)]
        dp[0][0][0] = grid[0][0]
        for k in range(1,2*n-1):
            for x1 in range(max(0,k-n+1),min(k+1,n)):
                y1 = k-x1 
                if grid[x1][y1] == -1:
                    continue
                for x2 in range(x1,min(k+1,n)):
                    y2 = k -x2 
                    if grid[x2][y2] == -1: continue
                    res = dp[k-1][x1][x2]
                    if x1:
                        res = max(res,dp[k-1][x1-1][x2])
                    if x2:
                        res = max(res,dp[k-1][x1][x2-1])
                    if x1 and x2:
                        res = max(res,dp[k-1][x1-1][x2-1])
                    res += grid[x1][y1]
                    if x2 != x1:
                        res += grid[x2][y2]
                    dp[k][x1][x2] = res
        return max(dp[-1][-1][-1],0)
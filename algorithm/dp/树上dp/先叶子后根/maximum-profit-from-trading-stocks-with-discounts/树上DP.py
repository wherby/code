# https://leetcode.cn/problems/maximum-profit-from-trading-stocks-with-discounts/description/3
# dp 表示子节点的状态，0表示没使用半价，1表示使用半价
# dp2表示转移矩阵， 0 的状态也是没有使用半价，1表示使用半价，但是如果不够，则其中节点的状态是由子节点的不使用半价得到的，因为父节点没有购买
#TIPS# 为什么用两个DP矩阵，因为DP表示子节点的状态merge，从子节点到根节点，这时候是状态转移，则需要另一个矩阵DP2计算所有可能的状态转移函数
from typing import List, Tuple, Optional



max = lambda a, b: b if b > a else a
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g= [[] for _ in range(n)]

        for a,b in hierarchy:
            g[a-1].append(b-1)

        def dfs(a):
            dp = [[0]*(budget+1) for _ in range(2)]

            for b in g[a]:
                tp = dfs(b)
                for i in range(budget,-1,-1):
                    for j in range(i+1):
                        dp[0][i] = max(dp[0][i], dp[0][i-j]+tp[0][j])
                        dp[1][i] = max(dp[1][i], dp[1][i-j]+tp[1][j])
            dp2 = [[0]*(budget+1) for _ in range(2)]
            for i in range(budget,-1,-1):
                if i >=present[a]:
                    dp2[0][i] = max(dp[0][i],dp[1][i-present[a]] -present[a] +future[a])
                else:
                    dp2[0][i] = dp[0][i]
                if i < present[a]//2:
                    dp2[1][i] =dp[0][i]
                else:
                    dp2[1][i] = max(dp[0][i],dp[1][i-present[a]//2] -present[a]//2 + future[a])
            #print(dp)
            return dp2
        #print(dfs(0))
        return dfs(0)[0][budget]





#re =Solution().maxProfit(n = 3, present = [49,10,27], future = [18,44,38], hierarchy = [[1,3],[1,2]], budget = 141)
#re =Solution().maxProfit(n = 3, present = [6,4,23], future =[50,48,17], hierarchy =[[1,3],[1,2]], budget = 28)
#re =Solution().maxProfit(n = 4, present = [35,9,6,8], future = [46,33,19,38], hierarchy = [[1,4],[4,3],[1,2]], budget = 67)
#re = Solution().maxProfit(n = 2, present = [1,2], future = [4,3], hierarchy = [[1,2]], budget = 3)

from input import n,present,future,hierarchy,budget
re = Solution().maxProfit(n , present , future , hierarchy , budget )
print(re)
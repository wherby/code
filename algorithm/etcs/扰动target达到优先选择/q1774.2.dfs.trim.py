# https://leetcode.cn/problems/closest-dessert-cost/submissions/
# DFS 剪枝
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        target -=0.001
        n = len(toppingCosts)
        mn  = baseCosts[0]
        def dfs(i,acc):
            nonlocal mn
            if i==n:
                if abs(target-mn)> abs(target-acc):
                    mn = acc
                return 
            if  abs(target-mn) < acc-target:
                return
            dfs(i+1,acc)
            dfs(i+1,acc + toppingCosts[i]*1)
            dfs(i+1,acc + toppingCosts[i]*2)
        for a in baseCosts:
            dfs(0,a)
        return mn
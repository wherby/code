# https://leetcode.cn/problems/maximum-amount-of-money-robot-can-earn/?envType=daily-question&envId=2026-04-02
from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m,n = len(coins),len(coins[0])
        @cache
        def dfs(i,j,res):
            
            if i >=m or j >=n or res <0:
                return -10**20
            a = coins[i][j]
            if i ==m-1 and j == n-1:
                if a <0 and res >0:
                    return 0 
                return a 
            ret = -10**20
            if a <0 and res >0:
                ret = max(ret, dfs(i,j+1,res-1),dfs(i+1,j,res-1))
            return max(ret,dfs(i,j+1,res)+a,dfs(i+1,j,res)+a)

        ret= dfs(0,0,2)
        dfs.cache_clear()
        return ret



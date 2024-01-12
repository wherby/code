# 
# https://leetcode.cn/contest/biweekly-contest-119/problems/number-of-possible-sets-of-closing-branches/

from typing import List, Tuple, Optional




class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        dp2 = [[10**10]*n for _ in range(n)]
        for a,b,c in roads:
            dp2[a][b] = min(dp2[a][b], c)
            dp2[b][a] = min(dp2[b][a], c)
        for i in range(n):
            dp2[i][i] = 0
        
        def verify(state):
            lef =set()
            for i in range(n):
                if state &(1<<i):
                    lef.add(i)
            dp = [[10**10]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i in lef and j in lef:
                        dp[i][j] = dp2[i][j]
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            for i in lef:
                for j in lef:
                    if dp[i][j] > maxDistance:
                        return False
            return True
        
        ret = 0
        for state in range(1<<n):
            if verify(state):
                #print(state)
                ret +=1
        #verify(15)
        return ret




re =Solution().numberOfSets(10,430,[[3,2,237],[3,1,79],[6,1,84],[6,1,103],[9,6,453],[3,1,342],[3,1,201],[8,0,439],[7,5,467],[4,3,99],[8,7,146],[8,7,335],[6,1,512],[1,0,498],[5,3,241],[5,2,202],[4,1,443],[2,0,69],[2,1,450],[6,3,352],[2,0,438],[4,0,95],[6,1,257],[5,1,271],[8,1,80],[9,1,452],[3,1,57],[9,7,361],[8,4,105]])
print(re)
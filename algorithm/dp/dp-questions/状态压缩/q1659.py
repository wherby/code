# https://leetcode.cn/problems/maximize-grid-happiness/
from functools import cache

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        score = [[0,0,0],
                 [0,-60,-10],
                 [0,-10,40]]
        tot = 3**n
        inner_score = [0]*tot
        inter_score = [[0]*tot for _ in range(tot)]
        mask_bit= [[0]*n for _ in range(tot)]
        iv_counter,ev_counter =[0]*tot,[0]*tot
        
        def init_data():
            for mask in range(tot):
                mask_tmp = mask
                for i in range(n):
                    x = mask_tmp %3 
                    mask_bit[mask][i] = x 
                    mask_tmp //=3 
                    if x ==1:
                        iv_counter[mask] +=1
                        inner_score[mask] += 120
                    elif x ==2:
                        ev_counter[mask] +=1
                        inner_score[mask] +=40
                    if i >0:
                        inner_score[mask] += score[x][mask_bit[mask][i-1]]
            for  i in range(tot):
                for j in range(tot):
                    for k in range(n):
                        inter_score[i][j] += score[mask_bit[i][k]][mask_bit[j][k]]
        init_data()
        @cache
        def dfs(row,preMask, iv,ev):
            if row == m or(iv ==0 and ev ==0):
                return 0
            res = 0
            for msk in range(tot):
                if iv_counter[msk] > iv or ev_counter[msk] > ev:
                    continue
                res = max(res, dfs(row +1, msk, iv - iv_counter[msk],ev - ev_counter[msk]) + inner_score[msk] + inter_score[preMask][msk])
            return res
        return dfs(0,0,introvertsCount,extrovertsCount)
    
re = Solution().getMaxGridHappiness(m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2)
print(re)
                        
        

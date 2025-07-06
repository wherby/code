# https://leetcode.cn/contest/weekly-contest-457/problems/minimum-moves-to-reach-target-in-grid/
# 如果从source->target 会有多种选择，反之则最多有2个路线
from functools import cache
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if sx == 0 and sy == 0 and ((sx!=tx) or (sy != ty)):
            return -1
        @cache
        def dfs(tx,ty):
            #print(tx,ty)
            if tx ==sx and ty == sy:
                return 0
            ret = 10**10
            if tx < sx or ty < sy:
                return ret
            if tx == ty:
                ret = min(ret, dfs(tx,0)+1,dfs(0,tx)+1)
            if tx > ty:
                if tx%2 ==0 and tx//2 >=ty:
                    ret = min(ret,dfs(tx//2,ty) +1)
                if tx-ty<=ty:
                    ret = min(ret,dfs(tx-ty,ty)+1)

                return ret
            else:
                if ty %2 == 0 and ty//2 >=tx:
                    ret = min(ret,dfs(tx,ty//2)+1)
                if ty-tx <=tx:
                    ret = min(ret,dfs(tx,ty-tx)+1)

                return ret

        ret = dfs(tx,ty)
        return ret if ret<10**10 else -1
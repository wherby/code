# https://leetcode.cn/problems/rMeRt2/
# https://leetcode.cn/problems/rMeRt2/solution/z-by-endlesscheng-6ver/

from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def Leetcode(self, words: List[str]) -> int:
        need = {
            "e":(8,7,4),
            "h":(7,1,1),
            "l":(5,3,3),
            "o":(3,3,2),
            "t":(2,1,1),
            "c":(1,1,1),
            "d":(0,1,1)
        }
        #"10011110111"
        FULL = int("10011110111",2)
        #print(FULL)
        costls= []
        for word in words:
            #print(word)
            cost ={}
            def dfs2(w,msk,cst):
                #print(w,msk,cst)
                if msk not in cost or cost[msk] > cst:
                    cost[msk] = cst
                for i,a in enumerate(w):
                    if a not in need:continue 
                    pos,m,limit = need[a]
                    if (msk>>pos) & m < limit:
                        dfs2(w[:i]+w[i+1:],msk + (1<<pos),cst + i*(len(w)-i-1))
            dfs2(word,0,0)
            costls.append(cost)
        MX = 10**9
        #print(costls)
        def merge(msk,add):
            for pos,m,limit in need.values():
                c1= (msk >>pos) &m 
                c2 = (add >>pos) & m
                if c1 +c2 > limit:return -1 
                msk = msk + (c2<<pos)
            return msk
        @cache
        def dfs(i,msk):
            if i == len(words):
                #print(msk,FULL)
                return 0 if msk == FULL else MX
            res = MX
            for add,cst in costls[i].items():
                if cst >= res :continue
                m = merge(msk,add)
                if m >=0:
                    res = min(res,cst + dfs(i+1,m))
            return res
        ans = dfs(0,0)
        return ans if ans<MX else -1

re =Solution().Leetcode(words = ["hold","engineer","cost","level"])
print(re)

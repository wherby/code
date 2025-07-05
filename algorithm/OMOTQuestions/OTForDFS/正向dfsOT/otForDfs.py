
from functools import cache

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9+7 
        ls = []
        word = word+ "*"
        lst = ""
        state = 0
        for a in word:
            if a != lst:
                if state>0:
                    ls.append(state)
                lst =a
                state = 1 
            else:
                state+=1
        n = len(ls)  
        #print(ls)
        @cache
        def dfs(res,idx):
            if idx == n :
                if res >0:
                    return 0 
                if res <= 0:
                    return 1 
            #print(res,idx)
            if res == 0:
                return   (ls[idx]  ) *dfs(0,idx+1) %mod
            ret = 0 
            
            for i in range(1,ls[idx]+1):
                ret += dfs(max(res - i,0), idx +1)
                ret %=mod
            return ret %mod 
        re = dfs(k,0)
        dfs.cache_clear()
        return re
from input import word
re =Solution().possibleStringCount(word,1292)
print(re)
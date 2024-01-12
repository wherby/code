# https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations/description/

from functools import cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def dfs(i,state,isused):
            if i ==n:
                return 1
            ret = 0
            im =1<<(ord(s[i]) - ord('a'))
            newM = im | state
            if bin(newM).count("1") <=k:
                ret = max(ret,dfs(i+1,newM,isused))
            else:
                ret = max(ret,dfs(i+1, im,isused)+1) 
            if  isused:
                return ret
            for j in range(26):
                im = 1<<j
                newM = state |im
                if bin(newM).count("1") <=k:
                    ret = max(ret,dfs(i+1,newM,True))
                else:
                    ret = max(ret,dfs(i+1, im,True)+1) 
            return ret 
        return dfs(0,0,False)
# https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations/submissions/671331730/?envType=daily-question&envId=2025-10-17
# 题目里是把一个小写字母转换到另一个小写字母，这时优化不能直接把小写字母转换为大写字母贪心求解，因为有可能会有k=25这种前后选择重复区域

from functools import cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k ==26:
            return 1
        n = len(s)
        @cache
        def dfs(i, used,state ):
            if i == n:
                return 1 
            ret = 0
            t1 = (ord(s[i]) -ord('a'))
            nst= (1<<t1) | state
            if nst.bit_count() == k+1:
                ret = max(ret, 1+dfs(i+1,used,1<<t1))
            else:
                ret = max(ret,dfs(i+1,used,nst))
            if used ==False :
                for j in range(26):
                    nst =(1<<j) | state
                    if nst.bit_count() == k+1:
                        ret = max(ret,dfs(i+1,True,1<<j) +1)
                    else: 
                        ret = max(ret,dfs(i+1,True,nst))
            
            return ret
        return dfs(0,False,0)


 
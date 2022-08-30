from functools import cache
class Solution(object):
    def countSpecialNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        ls = [int(i) for i in str(n)]
        m = len(ls)
        @cache
        def dfs(idx,mask,isNum,isFull):
            if idx ==m:return int(isNum)
            ret=0
            if not  isNum:
                ret += dfs(idx+1,mask,False,False)
            mx  = ls[idx] if isFull else 9
            for d in range(0 if isNum else 1, mx+1):
                if mask >>d &1 ==0:
                    ret  += dfs(idx+1,mask |(1<<d),True, isFull and d == mx)
            return ret
        return dfs(0,0,False,True)

print(Solution().countSpecialNumbers(20))
            

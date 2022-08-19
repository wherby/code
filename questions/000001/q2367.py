class Solution(object):
    def countSpecialNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        ls = [int(i) for i in str(n)]
        m = len(ls)
        @cache
        def dfs(idx,isTrival,isFull):
            nonlocal acc
            if idx ==m:return 1
            ret=0
            if isTrival:
                ret += 9*dfs(idx+1,False,False)
                dfs(idx+1,True,False)
            ret =0
            mx  = ls[i] if isFull else 9
            

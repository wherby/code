class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ls= [i for i in range(10)]
        tp=[]
        res =[]
        def dfs(idx,a):
            if idx ==n:
                c = 0
                for i in range(n):
                    c =c*10 + tp[i]
                res.append(c)
                return

            if a -k >=0:
                tp.append(a-k)
                dfs(idx+1,a-k)
                tp.pop()
            if a +k <10:
                tp.append(a+k)
                dfs(idx+1,a+k)
                tp.pop()
        for i in range(1,10):
            tp.append(i)
            dfs(1,i)
            tp.pop()
        res =list(set(res))
        return res

re = Solution().numsSameConsecDiff(n = 3, k = 7)
print(re)

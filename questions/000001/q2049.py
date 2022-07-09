class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        n = len(parents)
        ls = [[] for _ in range(n)]
        for i,a in enumerate(parents):
            if a !=-1:
                ls[a].append(i)
        child =[[] for _ in range(n)]
        mx = 0
        def dfs(node):
            c=1
            for a in ls[node]:
                t= dfs(a)
                child[node].append(t)
                c += t
            return c
        dfs(0)
        sm = n
        mx =0
        mxc = 0
        for i in range(n):
            ct  =child[i]
            res = sm - sum(ct) -1
            if res == 0:
                res =1
            for a in ct :
                res = res *a
            if res >mx:
                mx = res
                mxc =0
            if res == mx:
                mxc +=1
        return mxc
            

re = Solution().countHighestScoreNodes([-1,2,0,2,0])
print(re)
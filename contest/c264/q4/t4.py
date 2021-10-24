class Solution(object):
    def minimumTime(self, n, relations , time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        dp =[-1] * (n+2)
        g =[[] for i in range(n+1)]
        for re in relations:
            g[re[1]].append(re[0])
        #print(g)
        def dfs(n):
            if dp[n] != -1:
                return dp[n]
            if len(g[n]) ==0:
                dp[n] = time[n-1] 
                return time[n-1]
            mx = 0

            for i in g[n]:
                t = dfs(i)
                #print("t:" ,t)
                mx = max(mx,t)
            dp[n]= mx +time[n-1]
            return dp[n]
        for i in range(1,n+1):
            dfs(i)
        #print(dp)
        return max(dp)

relations = [[2,1]]

time = [10000,10000]
re=Solution().minimumTime(2,relations,time)
print(re)
import functools
class Solution(object):
    def waysToBuildRooms(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        n = len(prevRoom)
        ls =[[] for _ in range(n)]
        dp= [1]*n
        nums =[1]*n
        for i,a in enumerate(prevRoom):
            if a >=0:
                ls[a].append(i)
        pre= [1]*100001
        mod = 10**9+7
        for i in range(1,100001):
            pre[i] = pre[i-1] *i %mod
        @functools.lru_cache(None)
        def inv2(x):
            s= 1
            while x >1:
                s= s*(mod-mod//x)%mod
                x = mod%x
            return s
        def dfs(idx):

            if len(ls[idx]) ==0:
                nums[idx] =1
                dp[idx] =1
                return 1
            tls = []
            ksm = 1
            for t in ls[idx]:
                child = dfs(t)
                tls.append(child)
                ksm =ksm*dp[t]%mod
            sm= sum(tls)
            ksm = pre[sm] *ksm
            for t in tls:
                ksm = ksm *inv2(pre[t])
            dp[idx] = ksm %mod
            nums[idx] = 1+sm
            return 1+sm
        dfs(0)
        return dp[0]%mod

        




re = Solution().waysToBuildRooms(prevRoom =[-1,0,1,0,0,2,0,5,2,6])
print(re)
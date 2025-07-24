class Solution(object):
    def minimumScore(self, nums, edges):
        n = len(nums)
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        dp = [0]*n 
        ord=[[] for _ in range(n)]
        vs = [0]*(2*n)
        idx = 0
        def dfs(a,p):
            nonlocal idx
            idx1 = idx
            idx +=1
            acc =nums[a] 
            for b in g[a]:
                if b ==p : continue
                acc ^= dfs(b,a)
            dp[a] = acc
            vs[idx] =  vs[idx1]=  acc 
            ord[a] = [idx1,idx]
            idx +=1 
            return acc
        dfs(0,-1)
        ret = 10**20
        for a in range(1,n):
            ain,aout = ord[a]
            for b in range(a+1,n):
                b1,b2= ord[b]
                if ain<b1<b2<aout:
                    v1= dp[0]^dp[a]
                    v2 = dp[a]^ dp[b]
                    v3 = dp[b]
                elif b1<ain<aout <b2:
                    v1 = dp[0] ^ dp[b]
                    v2 = dp[b] ^ dp[a]
                    v3 = dp[a]
                else:
                    v1 = dp[0]^dp[a]^dp[b]
                    v2 = dp[a]
                    v3 = dp[b]
                vs = [v1,v2,v3]
                vs.sort()
                #print(vs,a,b)
                ret =min(ret, vs[-1] -vs[0])
        return ret


re = Solution().minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]])
print(re)
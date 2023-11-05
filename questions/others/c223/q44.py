import functools
class Solution:
    def minimumTimeRequired(self, jobs, k):
        N =len(jobs)

        @functools.lru_cache(None)
        def dfs(mask,basket):
            if mask ==0:
                return (1,0)
            ans =(float("inf"),float("inf"))
            for j in range(N):
                if mask & (1<<j):
                    pieces,last = dfs(mask- (1<<j),basket)
                    full = ((last + jobs[j]) >basket)
                    ans = min(ans,(pieces + full,jobs[j] + (1-full) * last))
            return ans
            
        lo,hi = max(jobs),sum(jobs)
        while lo <hi:
            mid = (lo+hi)>>1
            if dfs((1<<N)-1,mid)[0] >= k +1:
                lo = mid +1
            else:
                hi = mid
        return lo

j=[256,250,255,250,254,255,260,260,250,252,257,253]
k=9
re = Solution().minimumTimeRequired(j, k )
print(re)

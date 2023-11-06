from collections import defaultdict
import functools
from bisect import bisect_right,insort_left,bisect_left,bisect
class Solution:
    def maxTaxiEarnings(self, n, rides):
        slist = defaultdict(list)
        for s ,e ,t in rides:
            slist[s].append([s,e,t])
        
        ps = sorted(slist.keys())
        @functools.lru_cache(None)
        def solve(start =0):
            if start ==len(ps):
                return 0
            p_start = ps[start]
            to_ret = solve(start +1)
            for s,e,t in slist[p_start]:
                p_next = bisect(ps, e-0,1)
                to_ret = max(to_ret,t+e-s + solve(p_next))
            return to_ret
        return solve()


re =Solution().maxTaxiEarnings(10, [[9,10,2],[4,5,6],[6,8,1],[1,5,5],[4,9,5],[1,6,5],[4,8,3],[4,7,10],[1,9,8],[2,3,5]])
print(re)


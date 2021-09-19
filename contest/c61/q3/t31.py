#https://leetcode.com/contest/biweekly-contest-61/ranking  	pku_erutan  


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        s_list = collections.defaultdict(lambda:[])
        for s, e, t in rides :
            s_list[s].append([s, e, t])
        ps = sorted(s_list.keys())
        
        @functools.lru_cache(None)
        def solve(start=0) :
            if start == len(ps) :
                return 0
            p_start = ps[start]
            to_ret = solve(start+1)
            for s, e, t in s_list[p_start] :
                p_next = bisect.bisect(ps, e-.1)    
                to_ret = max(to_ret, t + e - s + solve(p_next))
            return to_ret
        return solve()
            
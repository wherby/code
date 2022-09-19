# https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ls = sorted(zip(quality,wage),key= lambda p: p[1]/p[0])
        ans = inf
        total = 0
        h = []
        for q,w in ls[:k-1]:
            total +=q
            heappush(h,-q)
        for q,w in ls[k-1:]:
            total +=q
            heappush(h,-q)
            ans = min(ans,w/q*total)
            total += heappop(h)
        return ans
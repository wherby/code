import heapq
class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        mx = 0
        st =[]
        for s,e,v in events:
            heapq.heappush(st,(e,v))
        ano = 0
        for s,e,v in events:
            while st and  s > st[0][0]:
                a,b = heapq.heappop(st)
                ano = max(ano,b)
            mx = max(mx,v +ano)
        return mx
        


re = Solution().maxTwoEvents([[10,83,53],[63,87,45],[97,100,32],[51,61,16]])
print(re)
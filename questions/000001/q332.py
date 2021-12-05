from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        g = defaultdict(list)
        for a,b in tickets:
            heapq.heappush(g[a],b)
        def visit(start,g):
            st = [start]
            route=[]
            while st:
                while g[st[-1]]:
                    st.append(heapq.heappop(g[st[-1]]))
                route.append(st.pop())
            route.reverse()
            return route
        return visit("JFK",g)


re = Solution().findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
print(re)

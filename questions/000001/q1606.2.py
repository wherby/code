# sortedList 
# https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests/
from heapq import heappop, heappush
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))  # sortedList
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])  # sortedList
                heappop(busy)
            if len(available) == 0:
                continue
            j = available.bisect_left(i % k)     # sortedList
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1
            heappush(busy, (start + t, id))
            available.remove(id)                    # sortedList
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]

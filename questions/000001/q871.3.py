import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        n = len(stations)
        ans,acc,h = 0,startFuel,[]
        for i in range(n+1):
            curr =stations[i][0] if i < n else target
            while acc<curr and h:
                acc -= heapq.heappop(h)
                ans +=1
            if acc < curr:
                return -1
            if i <n:
                heapq.heappush(h,-stations[i][1])
        return ans 
            
        
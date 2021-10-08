import heapq
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        stack =[]
        for c in trips:
            heapq.heappush(stack,(c[1],c[0],0))
            heapq.heappush(stack,(c[2]-0.01,c[0],1))
        res = 0
        while len(stack) >0:
            t = heapq.heappop(stack)
            if t[2] == 0:
                res +=t[1]
                if res > capacity:
                    return False
            else:
                res -=t[1]
        return True
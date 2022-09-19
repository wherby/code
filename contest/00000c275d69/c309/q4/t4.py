import heapq
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        stack =[(0,i) for i in range(n)]
        meetings.sort()
        ls = [0]*n
        for a,b in meetings:
            while a > stack[0][0]:
                x,y = heapq.heappop(stack)
                heapq.heappush(stack,(a,y))
            e,idx = heapq.heappop(stack)
            ls[idx] +=1
            endT = max(a,e) + b-a
            heapq.heappush(stack,(endT,idx))
        mx = 0
        idx =-1
        for i,a in enumerate(ls):
            if a > mx:
                mx = a
                idx = i
        return idx






re =Solution().mostBooked(n = 4, meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]])
print(re)
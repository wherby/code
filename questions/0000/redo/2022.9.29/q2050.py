import heapq
class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        g = [[] for _ in range(n)]
        inD = [0]*n
        for a,b in relations:
            g[a-1].append(b-1)
            inD[b-1]+=1
        st = []
        for i in range(n):
            if inD[i] ==0:
                heapq.heappush(st,(time[i],i))
        mx = 0
        while st:
            t,c = heapq.heappop(st)
            mx = max(mx,t)
            for a in g[c]:
                inD[a] -=1
                if inD[a] ==0:
                    heapq.heappush(st,(t + time[a],a))
        return mx
        
re =Solution().minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5])
print(re)
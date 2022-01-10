import heapq
class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        st = []
        mx =sum(plantTime) + max(growTime)
        n =len(plantTime)
        for i in range(n):
            heapq.heappush(st,(-growTime[i],plantTime[i]))
        res =0
        mx =0
        while st:
            g,p = heapq.heappop(st)
            res +=p
            mx = max(mx,res-g)
        return mx
re =Solution().earliestFullBloom([27,5,24,17,27,4,23,16,6,26,13,17,21,3,9,10,28,26,4,10,28,2],[26,9,14,17,6,14,23,24,11,6,27,14,13,1,15,5,12,15,23,27,28,12])
print(re)
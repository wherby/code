import heapq
class Solution:
    def minStoneSum(self, piles, k):
        piles = [-1* i for i in piles]
        heapq.heapify(piles)
        while k != 0:
            t1 = heapq.heappop(piles)
            t1 = t1 //2
            heapq.heappush(piles,t1)
            k -=1
        res =sum(piles)*-1
        return res

print(Solution().minStoneSum([4,3,6,7],3))

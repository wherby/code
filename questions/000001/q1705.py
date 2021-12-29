import heapq
class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        st =[]
        n = len(apples)
        cnt =0
        for i in range(50000):
            if i < n and apples[i]>0:
                heapq.heappush(st,(days[i] + i-1, apples[i]))
            while st and st[0][0] < i:
                heapq.heappop(st)
            if st:
                d,app = heapq.heappop(st)
               
                cnt +=1
                app -=1
                
                if app >0:
                    heapq.heappush(st,(d,app))
        return cnt

re = Solution().eatenApples(apples = [2,1,1,4,5], days = [10,10,6,4,2])
print(re)
            
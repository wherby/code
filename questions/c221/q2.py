
import heapq
class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        n =len(apples)
        q  =[]
        cnt =0
        for i in range(n):
            api = apples[i]
            d = days[i]
            if api >0:
                heapq.heappush(q,(d+i,api))
            while q:
                t,a = q[0]
                if t <=i:
                    heapq.heappop(q)
                else:
                    heapq.heappop(q)
                    cnt +=1
                    a -=1
                    if a>0:
                        heapq.heappush(q,(t,a))
                    break
        #print(cnt)
        for i in range(n,40000):
            while q:
                t,a = q[0]
                if t <=i:
                    heapq.heappop(q)
                else:
                    heapq.heappop(q)
                    cnt +=1
                    a -=1
                    if a>0:
                        heapq.heappush(q,(t,a))
                    break
        return cnt

re = Solution().eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2])
print(re)
            

#https://leetcode-cn.com/problems/number-of-orders-in-the-backlog/
import heapq
class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        buy =[]
        sell =[]
        for o in orders:
            if o[2] == 0:
                re = o[1]
                if not sell or sell[0][0] > o[0]:
                    heapq.heappush(buy,(-o[0],o[1],o[2]))
                else:
                    while sell and  sell[0][0]<= o[0] and re >0:
                        #print("x",sell)
                        s1 = heapq.heappop(sell)
                        if s1[1] > re:
                            r2 = s1[1]- re
                            heapq.heappush(sell, (s1[0],r2,s1[2]))
                            re=0
                        elif s1[1] < re:
                            re = re -s1[1] 
                        else:
                            re =0
                    if re >0:
                        heapq.heappush(buy,(-o[0],re,o[2]))
            else:
                re = o[1]
                if not buy or -buy[0][0] < o[0]:
                    heapq.heappush(sell,(o[0],o[1],o[2]))
                else:
                    while buy and  -buy[0][0]>= o[0] and re >0:
                        s1 = heapq.heappop(buy)
                        if s1[1] >re:
                            r2 = s1[1]-re
                            heapq.heappush(buy, (s1[0],r2,s1[2]))
                            re=0
                        elif s1[1] < re:
                            re = re -s1[1]
                        else:
                            re =0
                    if re >0:
                        heapq.heappush(sell,(o[0],re,o[2])) 
            #print(buy,sell,o)
        #print(buy,sell)
        cnt =0
        for b in buy:
            cnt += b[1]
            
        for s in sell:
            cnt += s[1]
        return cnt %(10**9+7)

#ords =[[1,29,1],[22,7,1],[24,1,0],[25,15,1],[18,8,1],[8,22,0],[25,15,1],[30,1,1],[27,30,0]]
#ords = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
ords = [[23,17,1],[18,27,0],[21,26,1],[8,17,0],[13,22,1],[22,21,1],[2,24,1],[5,7,0]]
re=Solution().getNumberOfBacklogOrders(ords)
print(re)
import heapq
class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        n = len(aliceValues)
        vals = []
        for i in range(n):
            heapq.heappush(vals,(-aliceValues[i]-bobValues[i],i))
        t = 0
        alice,bob = 0,0
        while vals:
            _,i = heapq.heappop(vals)
            if t %2 ==0:
                alice += aliceValues[i]
            else:
                bob  += bobValues[i]
            t +=1
        re = alice-bob
        #print(alice,bob)
        if re == 0 :
            return 0
        return 1 if re>0 else -1

re = Solution().stoneGameVI(aliceValues = [1,2], bobValues = [3,1])
print(re)
print(1^1,0^1)
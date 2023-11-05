import heapq
from bisect import bisect_right,insort_left,bisect_left

class Solution:

    def maxTaxiEarnings(self, n, rides) :
        dic ={0:0}
        def getDP(dp,x):
            endIndex = bisect_right(dp,x)
            return dic[dp[endIndex-1 ]]
        
        def clearDp(dp,x,y):
            endIndex = bisect_right(dp,x)
            n = len(dp)
            for i in range(endIndex,n):
                if getDP(dp,dp[i]) < y:
                    dic[dp[i]] =y
                else:
                    break
             

        rides = sorted(rides)
        dp =[0]
        for ride in rides:
            ride[2] = ride[1] - ride[0] + ride[2]
        endFirstTee=[0]
        valueTree =[[0,0,0]]
        #print(rides)
        for ride in rides:
            endIndex = bisect_right(endFirstTee,ride[1])
            #print(getDP(dp,ride[1]))
            #print(getDP(dp,ride[0]) + valueTree[endIndex-1][2])
            if getDP(dp,ride[0]) + ride[2] > getDP(dp,ride[1])  :
                #print("xx")
                if ride[1] not in dic:
                    insort_left(dp,ride[1])
                dic[ride[1]] =  getDP(dp,ride[0]) +ride[2]
                x = getDP(dp,ride[0]) + ride[2]
                clearDp(dp, ride[1],x)
            #print(dp)
                
        #print(dp,dic)
        return getDP(dp,n)



re =Solution().maxTaxiEarnings(10, [[9,10,2],[4,5,6],[6,8,1],[1,5,5],[4,9,5],[1,6,5],[4,8,3],[4,7,10],[1,9,8],[2,3,5]])
print(re)
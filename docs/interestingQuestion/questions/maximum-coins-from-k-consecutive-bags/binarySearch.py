from typing import List, Tuple, Optional


from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        pls =[0]
        for f,t,c in coins:
            pls.append(pls[-1]+ (t-f+1)*c)
        #print(pls,coins)
        n = len(coins)
        ret =0
        for i,(f,t,c) in enumerate(coins):
            at =f+k-1
            idx2 = bisect_right(coins,[at,10**10,0])
            acc = pls[idx2-1] -pls[i]
            mt = min(at,coins[idx2-1][1])
            acc += coins[idx2-1][2] * (mt - coins[idx2-1][0] +1)
            ret = max(ret,acc)
            at2 = t-k+1
            idx3 = bisect_left(coins,[at2,10**10,0])
            acc2 = pls[i+1] -pls[idx3]
            if idx3 != 0:
                if coins[idx3-1][0]<=at2 <= coins[idx3-1][1]:
                    acc2 += (coins[idx3-1][1] - at2+1)*coins[idx3-1][2]
            ret = max(ret,acc2)
            #print(acc,acc2,i,f,t,at2,at)
        return ret





#re =Solution().maximumCoins(coins = [[30,49,12]], k = 28)
re =Solution().maximumCoins(coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4)
print(re)
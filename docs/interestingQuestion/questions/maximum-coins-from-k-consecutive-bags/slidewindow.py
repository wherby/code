from typing import List, Tuple, Optional

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        def maxResultOnRight(coins):
            ans,l,acc =0,0,0 
            for a,b,c in coins:
                acc += (b-a+1)*c
                while coins[l][1]<b-k+1:
                    acc -= (coins[l][1] - coins[l][0] +1) *coins[l][2]
                    l +=1
                partialV = max(0,(b-k +1 -coins[l][0])) * coins[l][2]
                ans = max(ans,acc -partialV)
            return ans
        
        ans = maxResultOnRight(coins)

        for a in coins:
            a[0],a[1] = -a[1],-a[0]
        ans = max(ans, maxResultOnRight(coins[::-1]))
        return ans
    
#re =Solution().maximumCoins(coins = [[30,49,12]], k = 28)
re =Solution().maximumCoins(coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4)
print(re)

from input import coins,k
re =Solution().maximumCoins(coins,k)
print(re)

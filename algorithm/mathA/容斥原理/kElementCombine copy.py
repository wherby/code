from typing import List, Tuple, Optional
import math

def getKEle(ls):
    ret = [(1,-1)]
    for a in ls:
        for b,acc in list(ret):
            ret.append((math.lcm(a,b),acc*-1))
    return ret[1:]

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        l,r = 0, 10**20
        ls = getKEle(coins)
        def verify(mid):
            return sum([mid//a*acc for a,acc in ls]) >=k
        while l<r:
            mid = (l+r)>>1
            if verify(mid):
                r = mid 
            else:
                l = mid+1
            #print(mid)
        return l


re =Solution().findKthSmallest([20,6,15,16,22],25727)
print(re)
from typing import List, Tuple, Optional
import math

def getKEle(ls):
    n = len(ls)
    ret =[]
    for i in range(1,1<<n):
        lcm =1
        acc = -1
        for j in range(n):
            if (1<<j)&i:
                acc*=-1
                lcm = math.lcm(ls[j],lcm)
        ret.append((lcm,acc))
    print(ret)
    return ret

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        l,r = 0, 10**20
        ls = getKEle(coins)
        #print(ls)
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
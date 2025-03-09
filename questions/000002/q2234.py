from typing import List, Tuple, Optional
from collections import Counter


def fillFunc(ls, offer):
    ls.sort()
    n = len(ls)
    pre_sum= j =0
    while j < n and ls[j]*j <= pre_sum + offer:
        pre_sum += ls[j]
        j+=1
    return (pre_sum + offer) //j
    


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        ls = [max(0,target - a) for a in flowers]
        ls.sort()
        n = len(ls)
        if sum(ls)<=newFlowers:
            if ls[-1] ==0:
                return n*full
            return  max((n-1)*full + partial*(target-1), n*full)
        fullmost = 0
        res = newFlowers
        for a in ls:
            if a <= res:
                res -=a 
                fullmost +=1
            else:
                break
        fs = sorted(flowers)
        ret = 0
        l = presum = 0
        #print(res,ls,fs)
        for i in range(fullmost,-1,-1):
            while l <n-i and fs[l] *l <= presum + res:
                presum += fs[l]
                l +=1
            avg = (presum + res) //l
            ret = max(ret,i*full +avg*partial)
            #print(presum,res,l)
            res = res +  ls[i-1]
            #print(res,i,l,avg,ret,ls[i-1])
        return ret

re = Solution().maximumBeauty(flowers = [8,2], newFlowers = 24, target = 18, full = 6, partial = 3)
print(re)
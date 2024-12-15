from typing import List, Tuple, Optional

from heapq import heapify,heappop,heappush 


mod = 10**9 +7
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret


class Solution:
    def getFinalState(self, nums: List[int], k: int, mul: int) -> List[int]:
        if mul ==1:
            return nums
        st=[]
        for i,a in enumerate(nums):
            heappush(st,(a,i))
        mx = max(nums)
        while k and st[0][0]<mx:
            a,i = heappop(st)
            heappush(st,(a*mul,i))
            k -=1
        n = len(nums)
        m = k //n 
        res = k%n 
        ret = [-1]*n 
        mod = 10**9+7
        for j in range(n):
            a,i =heappop(st)
            a = quickPow(mul,m+int(j<res))*a %mod 
            ret[i] = a 
        return ret 

re = Solution().getFinalState(nums = [100000,2000], k = 2, mul= 1000000)
print(re)  
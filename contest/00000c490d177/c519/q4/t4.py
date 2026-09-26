



from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        
        
        def dfs(a, l ,r):
            nonlocal ans
            if len(a)<=1 or l ==r:
                return 
            mid = (l+r)>>1
            low = []
            high =[]
            c =[]
            d =[]
            for i,x in enumerate(a):
                if x <=mid:
                    while low and a[low[-1]]< x:
                        low.pop()
                    low.append(i)
                    c.append(x)
                else:
                    while high and a[high[-1]]>=x:
                        high.pop()
                    ans += len(low)
                    if high:
                        ans -= bisect_left(low,high[-1])
                    high.append(i)
                    d.append(x)
            dfs(c,l,mid)
            dfs(d,mid+1,r)
        sortedls = sorted(set(nums))
        ordLs = [bisect_left(sortedls,a ) for a in nums]
        ans = 0 
        dfs(ordLs,0,len(nums)-1)
        return ans

re =Solution().shadowPairs( nums = [3,1,4,2,5])
print(re)
            
            



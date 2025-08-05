
from typing import List, Tuple, Optional
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        mx = 0 
        for a in nums :
            mx |= a 
        st = []
        n = len(nums)
        ret = [0]*n
        for i,a in enumerate(nums[::-1]):
            tmp = []
            for b,idx in st:
                c = a|b 
                if tmp and c == tmp[-1][0]:
                    tmp.pop()
                tmp.append((c,idx))
            if tmp and a == tmp[-1][0]:
                tmp.pop()
            tmp.append((a,i))
            st = tmp
            ret[n-1-i] =i-st[0][1] +1 
            
        return ret
re  = Solution().smallestSubarrays(nums = [1,0,2,1,3])
print(re)
from typing import List, Tuple, Optional


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        ls = [(b,a) for a,b in zip(nums1,nums2)]
        ls.sort()
        #ls.sort()
        #print(ls)
        f  = [0]*(n+1)
        for i,(b,a) in enumerate(ls):
            for j in range(i+1,0, -1):
                f[j] = max(f[j],f[j-1] + a + b*j)
        
        s1 = sum(nums1)
        s2 = sum(nums2)
        print(f)
        for t,v in enumerate(f):
            if s1 + s2*t -v <= x:
                return t 
        return -1

re = Solution().minimumTime([4,4,9,10],[4,4,1,3],16)
print(re)
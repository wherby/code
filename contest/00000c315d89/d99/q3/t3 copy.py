from typing import List, Tuple, Optional


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        n = 1
        right = ranges[0][1]
        for a, b in ranges[1:]:
            if a <=right:
                right = max(b,right)
            else:
                right = b 
                n +=1
        #n = len(sp.span)-2
        #print(sp.span)
        mod = 10**9+7
        re = pow(2,n,mod)
        return re




re =Solution().countWays(ranges = [[0,2],[2,3]])
print(re)
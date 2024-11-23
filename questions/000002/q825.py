from typing import List, Tuple, Optional
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        cnt = 0
        l,r = 0,0
        c = Counter(ages)
        for a,b in c.items():
            if a <= a*0.5+7: continue 
            cnt += b*(b-1)
        for i,a in enumerate(ages):
            while r < i and ages[r] < ages[i] :
                r +=1
            while l<r and ages[l] <=0.5*a +7:
                l+=1
            cnt += r -l 
           # print(a,i,ages[l],ages[r],cnt)
        return cnt


re = Solution().numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110])
print(re)
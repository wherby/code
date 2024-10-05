# using range(10**19) will cauese isuue "OverflowError: Python int too large to convert to C ssize_t" https://bugs.python.org/issue41860
#
from typing import List, Tuple, Optional

from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def verify(mid):
            return sum([mid//a for a in time])>=totalTrips
        return bisect_left(range(10**18),True, key= verify) # if use range(10**19) there will have exception
    

re =Solution().minimumTime(time = [1,2,3], totalTrips = 50)
print(re)
from typing import List, Tuple, Optional

from sortedcontainers import SortedDict,SortedList


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic ={}
        for i,a in enumerate(nums2):
            dic[a] = i 
        n = len(nums1)
        tr1 = []
        for a in nums1:
            tr1.append(dic[a])
        cnt = 0
        #print(tr1)
        sl = SortedList([])
        for i, a in enumerate(tr1):
 
            k = sl.bisect_right(a)

            cnt += k*(n-a-1-(i-k))
            sl.add(a)
            #print(sl,sl2,cnt,k,a)
        return cnt



re =Solution().goodTriplets(nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3])
print(re)
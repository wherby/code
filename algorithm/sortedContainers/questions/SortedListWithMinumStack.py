# https://leetcode.cn/contest/weekly-contest-349/problems/maximum-sum-queries/
# Sortedlist with minimum stack
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from typing import List, Tuple, Optional



class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        qls = []
        n = len(queries)
        for i,(qx,qy) in enumerate(queries):
            qls.append((qx,qy,i))
        qls.sort(reverse= True)
        nums1 = [(x1,y1) for x1,y1 in zip(nums1,nums2)]
        nums1.sort()
        sl =SortedList([(10**10,-1)])
        ret = [0]*n

        #print(qls,nums1)
        for i in range(n):
            qx,qy,idx2 = qls[i]
            
            while nums1 and nums1[-1][0]>=qx:
                x1,y1 = nums1.pop(-1)
                #print(sl,x1,y1)
                idx1 = sl.bisect_right((y1,y1+x1))
                rm = []
                idx = idx1 -1
                while idx>=0 and sl[idx][1] < x1+y1:
                    rm.append(sl[idx])
                    idx -=1
                if x1+y1 > sl[idx1][1]:
                    #print(x1,y1,sl,idx)
                    sl.add((y1,x1+y1))
                for a in rm:
                    sl.remove(a)
                
            k = sl.bisect_left((qy,0))
            ret[idx2] = sl[k][1]
            #print(sl,k,qx,qy)
        
        return ret
            
        





#re =Solution().maximumSumQueries(nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]])
re =Solution().maximumSumQueries([3,2,5],[2,3,4],[[4,4],[3,2],[1,1]])
print(re)
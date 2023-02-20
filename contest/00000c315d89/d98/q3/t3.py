from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        nums.sort()
        cnt=0
        for a in nums:
            n1 = bin(a).count('1')
            clen =len(bin(a))-2
            if n1 ==1 and clen == cnt+1:
                cnt +=1
            elif clen == cnt:continue
            elif clen >cnt:
                return 2**cnt
            else:
                #print("aa")
                ls = bin(a)[2:]
                m = len(ls)
                for i in range(m-1,-1,-1):
                    if ls[i]=='1':
                        ls[i]='0'
                        break
                return int(''.join(ls))
        #print("nn")
        return 2**cnt
                
        





re =Solution().minImpossibleOR([2,1,3,4,5,6,7,13])
print(re)
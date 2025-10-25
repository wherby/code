from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        def nextPermutation(nums) :
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            if i >= 0:
                j = len(nums) - 1
                while j >= 0 and nums[i] >= nums[j]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        s1 = [ord(a) -ord('a') for a in s]
        s2 = [ord(a) -ord('a') for a in target]
        Equal = True
        n = len(s1)
        c = [0]*26
        for a in s1:
            c[a]+=1
        ret = []
        i=0
        while i<n:
            if Equal:
                b= s2[i]
                if c[b] != 0 :
                    c[b] -=1
                    ret.append(b)
                else:
                    fd = False
                    for idx in range(b+1,26):
                        if c[idx] != 0:
                            c[idx] -=1
                            ret.append(idx)
                            fd =True
                            Equal = False
                            break
                    if fd == False:
                        for j in range(25,-1,-1):
                            ret.extend([j]*c[j])
                        nextPermutation(ret)
                i=len(ret)

            else:
                for j in range(26):
                    if c[j] != 0 :
                        ret.extend([j]*c[j])
                break
        s3 = [chr(a+ord('a')) for a in ret]
        s3= "".join(s3)
        #print(s3)
        if s3 > target:
            return s3
        else:
            s3 = [a for a in s3]
            nextPermutation(s3)
            s3= "".join(s3)
            return s3 if s3>target else ""




re =Solution().lexGreaterPermutation("zqqqqqzz","zqqqzzzq")
print(re)

# 816   8162 8216
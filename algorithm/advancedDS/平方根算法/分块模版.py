# https://leetcode.cn/contest/weekly-contest-503/problems/number-of-pairs-after-increment/description/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
import math


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums2)
        bsize = int(math.sqrt(n)) if n >0 else 1 
        bnum = (n+bsize-1) // bsize 
        bc = [defaultdict(int ) for _ in range(bnum)]
        bacc = [0]*bnum 

        for i,a in enumerate(nums2):
            idx = i // bsize
            bc[idx][a] +=1
        def updateIdx(i):
            blk = i //bsize
            old = nums2[i]
            new = nums2[i] + val 
            bc[blk][old] -=1
            bc[blk][new] +=1
            nums2[i] = new 

        ret = []
        for q in queries:
            if q[0] == 1:
                _,x,y,val = q 
                start = x//bsize
                end = y //bsize 

                if start == end:
                    for i in range(x,y+1):
                        updateIdx(i)
                else:
                    for i in range(x,(start+1)*bsize):
                        updateIdx(i)
                    for i in range(start+1,end):
                        bacc[i] += val 
                    for i in range(end* bsize ,y+1):
                        updateIdx(i)
            else:
                tot = q[1]
                ans = 0 
                for x in nums1:
                    target = tot-x 

                    for i in range(bnum):
                        realV = target - bacc[i]
                        ans += bc[i][realV]
                ret.append(ans)
        return ret





re =Solution().numberOfPairs(nums1 = [1,1], nums2 = [2,2,3], queries = [[2,4],[1,0,1,1],[2,4]])
print(re)
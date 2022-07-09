# https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/

from collections import defaultdict
from functools import cache
class Solution:
    def lenLongestFibSubseq(self, arr) -> int:
        sa= set(arr)
        n = len(arr)
        dp={}
        for i in range(n):
            a = arr[i]
            for j in range(i-1,0,-1):
                b = arr[j]
                c = a-b
                if c>=b:continue
                if c in sa:
                    dp[(b,a)] = dp.get((c,b),2) +1
        if dp:
            return max(dp.values()) 
        return 0
        
re =Solution().lenLongestFibSubseq([2,4,5,6,7,8,11,13,14,15,21,22,34])
re =Solution().lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50])
re =Solution().lenLongestFibSubseq([2,3,4,1])
print(re)
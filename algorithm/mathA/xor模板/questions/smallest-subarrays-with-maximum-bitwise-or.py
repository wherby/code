# https://leetcode.cn/problems/smallest-subarrays-with-maximum-bitwise-or/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)

        dic = defaultdict(list)
        ret =[0]*n
        vls = [0]*n
        for i,a in enumerate(nums):
            ks = list(dic.keys())
            for k in ks:
                k2 = k |a 
                if k2 != k:
                    for b in dic[k]:
                        ret[b] = i-b+1
                    dic[k2].extend(dic[k])
                    del dic[k]
            dic[a].append(i)
            vls[i] = a 
            ret[i] =1
            #print(i,a, dic,ret)
        return ret
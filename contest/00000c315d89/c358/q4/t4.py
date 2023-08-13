from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] +=1
    #print(visited[:20])
    return visited

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod= 10**9+7
        n = len(nums)
        mx = max(nums)
        pls = get_prime(mx)
        dic = defaultdict(int)
        st = [-1]
        for i,a in enumerate(nums):
            while st[-1] != -1 and pls[a]>pls[nums[st[-1]]]:
                b = st.pop()
                dic[nums[b]] += (i-b) *(b - st[-1])
            st.append(i)
            #print(i,a,st,pls[a])
        
        #print([pls[a] for a in nums])
        #print(st,dic)
        while st and st[-1] != -1:
            b = st.pop()
            dic[nums[b]] += (n-b) *(b - st[-1])
        kvls = [(k,v) for k,v in dic.items()]
        kvls.sort()
        acc =1
        #print(kvls)
        while k >0:
            k1,v1= kvls.pop()
            v2 = min(v1,k)
            k-= v2
            acc *= pow(k1,v2,mod)
            acc %=mod 
        return acc
            
        




#re =Solution().maximumScore(nums = [19,12,14,6,10,18], k = 3)
re = Solution().maximumScore([1,63726,98774,48343,54306,45948,26335,88745,60289,94170,55909,38119,87780,65274,84854,77713,53841,60720,71460,37862,40291,61138,98670,79170,93499,28470,45014,71610,72874,46410,87146,50685,7623,10503,78540,1,28140,74412,22770,60060,72150,53231,89994,48246,67453,1,1,47819,1,23926],4)
print(re)
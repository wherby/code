from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        dic = defaultdict(int)
        l = 0
        result =[]
        m = len(word)
        for i,a in enumerate(word):
            if i >0 and abs(ord(a) - ord(word[i-1])) >2:
                while l <i-1:
                    b = word[l]
                    dic[b] -=1
                    if dic[b] ==0:
                        del dic[b]
                    #print(dic)
                    if (i-l ) == len(dic)*k and l!=i:
                        result.append([l,i])
                    l +=1
                l = i
            dic[a] +=1
            while dic[a] > k:
                b = word[l]
                dic[b] -=1
                if dic[b] ==0:
                    del dic[b]
                l+=1
            if (i-l +1) == len(dic)*k:
                result.append([l,i])
        while l<m:
            
            b = word[l]
            dic[b] -=1
            if dic[b] ==0:
                del dic[b]
            #print(dic)
            l+=1
            if (m-l ) == len(dic)*k  and l != m:
                result.append([l,i])
            
        # cnt = 0
        # result.sort()
        # n = len(result)
        # idx = 0
        #print(result)
        # while idx<n:
        #     st = idx+1
        #     while st <n and result[st][0] == result[idx][0]:
        #         st +=1
        #     for i in range(idx+1,st):
        #         result[i][0]=result[idx][1]+1
        #     cnt +=st-idx
        #     idx +=1
            #print(result)
        return len(result)
            
        




re =Solution().countCompleteSubstrings(word = "abb", k = 2)
print(re)
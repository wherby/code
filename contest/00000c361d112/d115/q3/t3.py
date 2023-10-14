from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        dic= defaultdict(list)
        for i,a in enumerate(words):
            dic[a].append(i)
        def diff(a,b):
            return len([x for x,y in zip(a,b) if x!=y]) ==1
        @cache
        def dfs(idx):
            if idx ==n:
                return 0
            mx = 1
            for i in range(idx+1,n):
                if len(words[i]) == len(words[idx]) and groups[i] != groups[idx] and diff(words[i],words[idx]) ==1 :
                    mx = max(mx,1 + dfs(i))
            return mx
        mx= 0 
        mxn = -1
        for i in range(n):
            if dfs(i)>mx:
                mxn = i 
                mx = dfs(i)
        ret =[words[mxn]]
        #print("cc")
        while dfs(mxn) !=1:
            for i in range(mxn+1,n):
                if dfs(i) == mx -1 and len(words[i]) == len(words[mxn]) and groups[mxn] != groups[i] and diff(words[i],words[mxn]) ==1:
                    ret.append(words[i])
                    mxn = i
                    mx = mx-1
                    break
        return ret
                    
        





re =Solution().getWordsInLongestSubsequence(4,["dcaacc","da","ddcbd","dd"],[2,3,1,4])
print(re)
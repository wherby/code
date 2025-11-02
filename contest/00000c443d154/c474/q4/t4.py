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
from collections import Counter
from string import ascii_lowercase
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(target)
        hf = n //2
        odv = ""
        c = Counter(s)
        left = Counter()
        mxs = []
        for k,v in c.items():
            left[k] = v //2 
            if v%2 ==1:
                if odv != "":
                    return ""
                odv =k
        for j in range(25,-1,-1):
            ch = ascii_lowercase[j]
            mxs.extend(ch * left[ch])
        mxs = "".join(mxs)
        #print(mxs)
        def nextString(target):
            for a in target[:n//2]:
                left[a] -=1
            ans = list(target[:hf])
            for i in range(hf-1,-1,-1):
                c1 = target[i]
                left[c1]+=1
                if any(cnt < 0 for cnt in left.values()):
                    continue 
                for j in range(ord(c1) - ord('a') + 1, 26):
                    ch = ascii_lowercase[j]
                    if left[ch] == 0:
                        continue

                    left[ch] -= 1
                    ans[i] = ch
                    del ans[i + 1:]

                    for ch in ascii_lowercase:
                        ans.extend(ch * left[ch])
                    return ''.join(ans)
            return ""
        mt = nextString(target)
        if mt =="":
            t1 = mxs + odv + mxs[::-1]
            if t1>target:
                return t1 
            else:
                return ""
        return mt + odv + mt[::-1]



re =Solution().lexPalindromicPermutation(s = "aabb", target = "abaa")
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from collections import Counter
def comb2(n,m):
    cnt = 1
    for i in range(m):
        cnt *=n-i
        cnt //= i+1
    return cnt

    
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        mod = 10**9+7
        ds=Counter(s)
        small_letters = list(map(chr, range(ord('a'), ord('z')+1)))
        dic = defaultdict(list)
        for a in small_letters:
            dic[ds[a]].append(a)
        if len(ds.keys()) <k:
            return 0
        keys = list(dic.keys())
        keys.sort()
        acc =1
        while k >0 and keys:
            a = keys.pop()
            ns = len(dic[a])
            if a ==0:continue
            #print(a,ns,k)
            if ns<=k:
                k -= ns
                acc = acc*pow(a,ns,mod) %mod 
            else:
                
                acc = acc* comb2(ns,k) *pow(a,k,mod)%mod
                k = 0
            #print(acc,ns,k)
        return acc



re =Solution().countKSubsequencesWithMaxBeauty("kubawiihlmnrlpcydtsffwwfkyyanjyswxmxa",32)
print(re)
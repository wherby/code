from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        starN,endN= [[] for _ in range(26)],[[] for _ in range(26)]
        for i,w in enumerate(words):
            sidx = ord(w[0]) - ord('a')
            eidx = ord(w[-1])- ord('a')
            starN[sidx].append(i)
            
            endN[eidx].append(i)
        tlen = sum([len(a) for a in words])
        rm = {}
        cnt  = 0 
        couldRm = True
        acc =0 
        #print(starN,endN)
        while couldRm:
            acc += 1
            if acc>10:return
            #print(rm)
            couldRm = False
            for i in range(26):
                if couldRm:break
                for k in starN[i]:
                    if couldRm:break
                    if k in rm: continue
                    for m in endN[i]:
                        #print(m,k,words)
                        if m in rm:continue
                        if k != m:
                            rm[k] = 1
                            rm[m] =1
                            cnt +=1
                            couldRm = True
                            newS = words[m] + words[k][1:]
                            words.append(newS)
                            sidx = ord(newS[0]) - ord('a')
                            eidx = ord(newS[-1])- ord('a')
                            starN[sidx].append(n)
                            endN[eidx].append(n)
                            n +=1
                            break
        return tlen - cnt




re =Solution().minimizeConcatenatedLength(words =["aca","b","baa"])
print(re)
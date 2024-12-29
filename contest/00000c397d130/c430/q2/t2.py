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
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends ==1:
            return word
        n = len(word)
        tlen = n-numFriends+1
        aToZ ='abcdefghijklmnopqrstuvwxyz'
        dic = defaultdict(int)
        for i,a in enumerate(aToZ):
            dic[a] =i 
        stDic = {}

        def ord(mid):
            dic = defaultdict(list)
            if mid ==1:
                for i,a in enumerate(word):
                    dic[a].append(i)
                stDic[mid] = getKeyOrder(dic)
            else:
                hf = mid//2
                dic = defaultdict(list)
                for i in range(n-mid +1):
                    a = stDic[hf][i]
                    b = stDic[hf][i+hf]
                    k = a *1000+b 
                    dic[k].append(i)
                stDic[mid] = getKeyOrder(dic)

        def getKeyOrder(dic):
            keys =list(dic.keys())
            keys.sort()
            ret ={}
            for i,k in enumerate(keys):
                for a in dic[k]:
                    ret[a] = i
            return ret
        cur = 1
        while cur <= n:
            ord(cur)
            cur =cur*2
        binR = str(bin(tlen))[2:]
        m = len(binR)
        cand = set([])
        dic =defaultdict(list)

        for i,a in enumerate(word):

            dic[stDic[1][i]].append(i)
        ks = list(dic.keys())
        ks.sort()
        for a in dic[ks[-1]]:
            cand.add(a)
        print(cand,dic)
        
        acc =0
        for i,a in enumerate(binR[::-1]):
            tmp =set([])
            if a == "1":
                t = 1<<(m-i-1)
                ks = list(stDic[t].keys())
                dic= defaultdict(list)
                for b in cand:
                    if b+acc+t <=n:
                        #print(t,b+acc)
                        dic[stDic[t][b+acc]].append(b)
                ks = list(dic.keys())
                ks.sort()
                print(t,cand)
                #print(ks,t,acc,cand)
                if len(ks) ==0:
                    re = list(cand)[0]
                    return word[re:re+tlen]
                 
                for b in dic[ks[-1]]:
                    tmp.add(b)
                cand = tmp
                acc += t
                
            else:
                pass
        re = list(cand)[0]
        return word[re:re+tlen]




re =Solution().answerString(word = "nbjnc", numFriends = 2)
print(re)
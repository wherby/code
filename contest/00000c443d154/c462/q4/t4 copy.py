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
import itertools


ls= []

for a in range(1,10):
    ls.append((str(a)*a,1<<a))


def allState(k,m):
    ret=[]
    state = (1<<k) -1
    while (state <(1<<m)):
        ret.append(state)
        c = state &(-state)
        r = state +c
        state= (((r ^ state) >>2)//c) |r 
    return ret

def getNext(ls):
    cand = []
    for a,s1 in ls:
        if len(a)>=15:
            continue
        t =""
        if len(a)%2 ==1:
            t =a[len(a)//2]
        cand.append((a[:len(a)//2],s1,t))

    tls = []
    for a,s1,t in cand:
        for i in range(2,10,2):
            if (1<<i) &s1:
                continue
            n1 = len(a)
            m= n1 + i //2 
            if m > 7:continue
            astat = allState(i//2,m)
            for as1 in astat:
                re =""
                idx =0
                for j in range(m):
                    if as1 &(1<<j):
                        re += str(i)
                    else:
                        re += a[idx]
                        idx +=1
                tls.append((re +t + re[::-1] ,s1 + (1<<i)))
    return tls
ls1 = list(ls)
while len(ls1):
    ls1 = getNext(ls1)
    for a in ls1:
        ls.append(a)

ls =[int(a[0]) for a in ls]
ls.sort()

class Solution:
    def specialPalindrome(self, n: int) -> int:

        idx =bisect_right(ls,n)
        print(len(ls))
        print(len(set(ls)))
        return ls[idx]







re =Solution().specialPalindrome(682125)
print(re)
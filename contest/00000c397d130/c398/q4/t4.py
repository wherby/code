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

mod = 10**9+7
N = 10**5
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret


prels = [1]*(N+1)

def getInvArray(n,mod = 10**9+7):
    inv = [1]*(n+1)
    acc = 1
    for i in range(1,n+1):
        acc =acc*i%mod
        prels[i] = acc
    inv[-1] = quickPow(acc,mod-2)
    for i in range(n-1,-1,-1):
        inv[i] = inv[i+1]*(i+1) %mod
    return inv

def inv(x):
    return quickPow(x,mod-2)
invls = getInvArray(10**5)
def comb2(n,m, mod= 10**9+7):
    cnt = prels[n]* invls[n-m] * invls[m] %mod
    return cnt
    
class Solution(object):
    def waysToReachStair(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 2

        ac= k-1
        ls =[]
        while ac:
            ls.append(ac%2)
            ac = ac//2
        m = len(ls)
        acc =0
        for i,a in enumerate(ls):
            if a ==0:
                acc += 1<<i
        if acc > m+1:
            return 0
        ret =0
        for j in range(1,20):
            t1 = 0
            for k in range(j):
                t1 += 1<<(m+k)
            #print(t1,acc,m+j+1)
            if acc + t1 <= m+j+1:
                ret += comb2(m+j+1,acc +t1)
                #print("cc")

        #print(m,acc)
        return comb2(m+1,acc)+ret
        




re =Solution().waysToReachStair(1)
print(re)
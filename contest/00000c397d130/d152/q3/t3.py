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

import time


import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        t0 = time.perf_counter()
        result = func(*args,**kwargs)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_list =[]
        if args:
            arg_list.append( ", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['{0} = {1}'.format(k,w) for k,w in sorted(kwargs.items())]
            arg_list.append(", ".join(pairs))
        arg_str = ", ".join(arg_list)
        #print('[{0}] {1}({2}) -> {3}' .format( elapsed, name, arg_str,str(result)))
        print(elapsed)
        return result
    return clocked


class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod

class Solution:

    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        dic = defaultdict(int)
        sl = SortedList([])
        for word in words:
            sh = StringHash(word)
            n = len(word)
            for  i in range(1,n+1):
                t = sh.query(0,i)
                dic[(t,i)]+=1
                if dic[(t,i)] >=k:
                    sl.add((i,t,dic[(t,i)]))
        m = len(words)
        ret = [0]*m
        #print(sl)
        if len(sl)==0:
            return ret 
        ll,tar,kk =sl[-1]
        if kk >k:
            ret = [ll] *m
            return ret
        for j,word in enumerate(words):
            sh = StringHash(word)

            if len(word)<ll or sh.query(0,ll) !=tar:
                ret[j] = ll 
            else:
                n = len(word)
                for i in range(1,n+1):
                    t = sh.query(0,i)
                    if dic[(t,i)]>=k:
                        sl.remove((i,t,dic[(t,i)]))
                    dic[(t,i)] -=1
                #print(sl)
                if len(sl)>0:
                    ret[j]= sl[-1][0]
                for i in range(1,n+1):
                    t = sh.query(0,i)
                    dic[(t,i)] +=1
                    if dic[(t,i)]>=k:
                        sl.add((i,t,dic[(t,i)]))
        return ret





re =Solution().longestCommonPrefix( words = ["a"*100 for _ in range(10**4)], k = 56)
#print(re)
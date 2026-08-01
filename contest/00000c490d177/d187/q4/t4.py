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
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(target)
        if len(source) != n :
            return -1 
        hashTar = StringHash(target)
        match_rule = [[] for _ in range(n)]
        
        for idx in range(len(rules)):
            pat = rules[idx][0]
            rep = rules[idx][1]
            cost= costs[idx] + pat.count("*")
            L = len(pat)
            sh_t = StringHash(rep).query(0,L)
            for i in range(n-L+1):
                if hashTar.query(i,i+L) == sh_t:
                    match_rule[i].append((idx,cost))
        #print(match_rule)
        @cache
        def dfs(i):
            if i == n :
                return 0 
            ret = 10**20 
            
            if source[i] == target[i]:
                ret = min(ret,dfs(i+1))
            
            for idx,cost in match_rule[i]:
                pat = rules[idx][0]
                L = len(pat)
                
                matched = True
                for j in range(L):
                    if pat[j] !="*" and pat[j] != source[i+j]:
                        matched = False
                        break
                if matched:
                    ret = min(ret, dfs(i+L)+cost)
            return ret 
        res =  dfs(0)
        dfs.cache_clear()
        return res if res <10**20 else -1


re =Solution().minCost(source = "cat", target = "dog", rules = [["c*t","dog"]], costs = [2])
print(re)
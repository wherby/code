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

class Trie:
    def __init__(self):
        self.children = [None]*26
        self.isEnd =False
        self.cnt = 0
    
    def insert(self,word):
        node = self
        self.cnt +=1
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
            node.cnt +=1
        node.isEnd = True
        
    def find(self,ch):
        ch = ord(ch) - ord('a')
        return self.children[ch]
    
    
    def dfs(self,word,start):
        if start == len(word):
            return True
        node =self
        for i in range(start,len(word)):
            node = node.children[ord(word[i]) -ord('a')]
            if node is None:
                return False
            if node.isEnd and self.dfs(word,i +1):
                return True
        return False

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        tr = Trie()
        for word  in words:
            tr.insert(word)
        
        dic = {}
        for w,c in zip(words,costs):
            dic[w]= min(c,dic.get(w,10**10))
        #print(dic)
        n = len(target)
        @cache
        def dfs(i):
            if i == n:
                return 0
            tr1 = tr
            j = i
            ret = 10**10
            while tr1 != None and j <n:
                tr1 = tr1.find(target[j])
                j+=1
                if tr1 != None and tr1.isEnd==True:
                    ret = min(ret,dic[target[i:j]] + dfs(j))
            return ret
        ret = dfs(0) 
        return ret if ret<10**10 else -1   




re =Solution().minimumCost( target = "r", words = ["r","r","r","r"], costs = [1,6,3,3])
print(re)
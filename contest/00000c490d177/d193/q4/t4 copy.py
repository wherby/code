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
from itertools import permutations
class TrieNode:
    def __init__(self):
        self.idx = -1
        self.children = {}

class Solution:
    def minInversions(self, words: list[str], target: list[int]) -> int:
        n = len(words)
        
        pos = [0] * n 
        for i, a in enumerate(target):
            pos[a] = i
        
        root = TrieNode()
        for i, word in enumerate(words):
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.idx = i 
        
        ans = 0
        def dfs(node):
            nonlocal ans 
            
            cur = []
            if node.idx != -1:
                cur.append(pos[node.idx])
            
            child = []
            for ch in node.children.values():
                child.append(dfs(ch))
            if node.idx != -1:
                for ch_list in child:
                    for y in ch_list:
                        if pos[node.idx] >y:
                            ans += 1
            m = len(child)
            if m > 1:
                dp = [[0] * m for _ in range(m)]
                for i in range(m):
                    for j in range(m):
                        if i == j:
                            continue
                        sl = SortedList(child[j])
                        inv = 0
                        for x in child[i]:
                            inv += sl.bisect_left(x)
                            
                        dp[i][j] = inv
                
                memo = [10**20] * (1 << m)
                memo[0] = 0
                
                for mask in range(1 << m):
                    if memo[mask] ==10**20:
                        continue

                    for k in range(m):
                        if not (mask & (1 << k)):
                            add_cost = 0
                            for u in range(m):
                                if mask & (1 << u):
                                    add_cost += dp[u][k]
                            next_mask = mask | (1 << k)
                            if memo[mask] + add_cost < memo[next_mask]:
                                memo[next_mask] = memo[mask] + add_cost
                
                ans += memo[(1 << m) - 1]
                
            for ch in child:
                cur.extend(ch)
            return cur 

        dfs(root)
        return ans
                



words = ["dda","cghdacdbgjdf","jhfaagihadddibfc","fe","ghbgibhj","be","cfegbagbfecdcch","ceaijggfeiejcf","ifcajedjjae","dadff","icg","ajjicdjgacigj","gca","aggeabhdjibbi","dadgihjaaabfc","hfjh","ehdfbhcccdcgedab"]
target = [11,9,3,8,15,6,5,13,4,2,7,14,16,0,10,12,1]

words = ["cgaihbagcgdfiafc","fijehgc","ghadajdbcfhgf","ijgbcicjdjeah","feebfehgabgd"]
target = [2,1,3,0,4]
words = ["cffbgagbjdbjdac","acbhh","f","jhbgijfgbjbffhhc","jicjb","ibfejdcijiicgjd","ehijebdeifbgacjejg","abbaghigihd","ajjdjicgcdjiha","jfaddhfjhbdedbcjg","efgb","idebdhfdce","ciagb","jbih","gbbbeehfgbheedaag","gadebiadeaeicbbbhe","ibbddef","ggiaeieb","cfjdjfiadcdcj","cediadejcafiiaj","ciigchghebfgbg","hdifhgdaeggghejeh","i","ccadgddjacchief","efgaffdfbhf","acfahgafabfcf","edcbaihc","jbabifccjhfbcegcjib","hfbcaccfeaihf","dcdfdjhgbddj","ebajicebfbjbeefd","g","jdgjgedeaeiidcj","iggfgbcifgbfijaahiej","cacab","ifhghfbd","icebgcihecffgagfj"]
target = [6,7,29,2,13,5,16,9,23,11,25,4,14,34,33,28,10,18,26,36,15,20,3,8,12,0,31,32,19,22,21,30,17,27,35,1,24]
re =Solution().minInversions(words = ["bad","bag","fig","fed"], target = [3,1,0,2])
print(re)
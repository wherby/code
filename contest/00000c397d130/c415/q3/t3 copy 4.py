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


def calculate_z_array(s):
    N = len(s)
    Z = [0] * N
    L, R = 0, 0
    for i in range(1, N):
        if i > R:
            L = R = i
            while R < N and s[R - L] == s[R]:
                R += 1
            R -= 1
            Z[i] = R - L + 1
        else:
            k = i - L
            if Z[k] + i <= R:
                Z[i] = Z[k]
            else:
                L = i
                while R < N and s[R - L] == s[R]:
                    R += 1
                R -= 1
                Z[i] = R - L + 1
        #print(i,L,R,Z)
    return Z

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        dic= defaultdict(set)
        target = target + "A"*10000
        for word in words:
            m = len(word)
            cand = [i for i in range(n) if word[0] == target[i]]
            for i in range(m):
                cand =[j for j in cand if word[i] == target[j+i]]
                for a in cand:
                    dic[a+i+1].add(i+1)
                if len(cand) ==0:
                    break
        #@print(dic)
        cnt = 0 
        cand =[n]
        visit ={}
        while cand:
            tmp = set()
            for a in cand:
                if a == 0:
                    return cnt
                if a in visit:
                    continue
                visit[a] = 1
                for b in dic[a]:
                    tmp.add(a-b)
            cnt +=1
            cand = tmp
        return -1



re =Solution().minValidStrings(words = ["abc","aaaaa"*100,"bcdef"], target = "aaaa"*1000)
print(re)
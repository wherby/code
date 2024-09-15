# https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/submissions/564866595/
# contest/00000c397d130/c415/q3

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

from vars import words,target

re =Solution().minValidStrings(words, target )
print(re)
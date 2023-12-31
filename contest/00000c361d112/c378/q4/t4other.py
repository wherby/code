from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
from collections import Counter
from itertools import accumulate

## https://leetcode.cn/problems/palindrome-rearrangement-queries/solutions/2585862/fen-lei-tao-lun-by-endlesscheng-jxg0/

def getPre(s):
    pre = [[0 for _ in range(26)]]
    for a in s:
        pre.append(list(pre[-1]))
        pre[-1][ord(a)- ord('a')] +=1
    return pre

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n2 = len(s)
        n = n2//2
        t = s[n:][::-1]
        s = s[:n]
        pres ,pret = getPre(s),getPre(t)
        
        preNe = list(accumulate((x!=y for x,y in zip(s,t)),initial =0))
        
        def count(pre,l,r):
            return [x-y for x,y in zip(pre[r+1],pre[l])]
        
        def remove(c1,c2):
            for i,k in enumerate(c2):
                c1[i] -= k 
                if c1[i] <0:
                    return None 
            return c1
        
        def check(l1,r1,l2,r2,pres,pret):
            #print(l1,r1,l2,r2)
            if preNe[l1] >0 or preNe[n] - preNe[max(r1,r2)+1] >0:
                #print("1",preNe,l1,r1,r2)
                return False
            
            if r2 <= r1:
                if count(pres,l1,r1) != count(pret,l1,r1):
                    return False
            elif r1 < l2:
                if preNe[l2]-preNe[r1+1] >0 or count(pres,l1,r1) != count(pret,l1,r1) or count(pres,l2,r2) != count(pret,l2,r2):
                    #print("1",preNe,l1,r1,r2,count(pres,l1,r1) , count(pret,l1,r1),count(pres,l2,r2) != count(pret,l2,r2),preNe[l2]-preNe[r1+1] >0)
                    return False
            else:
                s1 =remove(count(pres,l1,r1), count(pret,l1,l2-1))
                s2 =remove(count(pret,l2,r2),count(pres,r1+1,r2))
                if s1 == None or s2 ==None or s1 !=s2:
                    #print("1",preNe,l1,r1,l2,r2,s1,s2,count(pres,l1,r1),count(pret,l1,r2-1))
                    return False
            return True
        
        ret = []
        for a,b,c,d in queries:
            c,d = n2-1-d,n2-1-c
            tmp = check(a,b,c,d,pres,pret) if a <= c else check(c,d,a,b,pret,pres)
            ret.append(tmp)
        return ret                 
        





#re =Solution().canMakePalindromeQueries("odaxusaweuasuoeudxwa",[[0,5,10,14]])
re =Solution().canMakePalindromeQueries(s = "acbcab", queries = [[1,2,4,5]])
print(re)
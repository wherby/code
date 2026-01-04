# contest/00000c443d154/c483/q4
# https://leetcode.cn/problems/minimum-cost-to-merge-sorted-lists/
# https://leetcode.com/contest/weekly-contest-483/problems/minimum-cost-to-merge-sorted-lists/submissions/1873803244/
# 使用位数划分，把状态分解 使得满状态 2**N 划分减少一半计算, 最终得到 2**N 复杂度， 如果没有减少1/2 则需要 N*（2**N)的复杂度
from typing import List, Tuple, Optional

from functools import cache


from bisect import bisect_right,insort_left,bisect_left


import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print('[{0}] {1}' .format( elapsed, name))
        return result
    return clocked

from input import lists,lists2

import itertools
class Solution:
    @clock
    def minMergeCost(self, lists: List[List[int]]) -> int:

        n = len(lists)
        acc =0
        @cache
        def getMd(sa):
            nonlocal acc 
            #print(sa)
            acc+=1
            la=[]
            for i in range(n):
                if (1<<i) &sa:
                    la.append(i)
            m = 0 
            for a in la:
                m +=len(lists[a])
            l = min(lists[a][0] for a in la)
            r = max(lists[a][-1] for a in la)
            while l <r:
                #print(l,r)
                md = (l+r)//2 
                cnt =0
                for a in la:
                    cnt += bisect_right(lists[a] ,md)
                if cnt >= (m+1)//2:
                    r = md 
                else:
                    l = md+1
            #print(m,l,cnt,la)
            return m,l

        @cache 
        def dfs(state):
            res = 10**30
            la  = []
            for i in range(n):
                if (1<<i) & state:
                    la.append(i)
            if len(la) ==1:
                return 0
            m = len(la)
            m = m //2
            cand =[]
            
            for i in range(1,m+1):
                ls = itertools.combinations(la,i)
                for l1 in ls:
                    acc = 0 
                    for b in l1:
                        acc +=1<<b
                    cand.append(acc)
            #print(m,cand,state,la)
            for c1 in cand:
                l1,v1 = getMd(c1)
                l2,v2 = getMd(state-c1)
                #print(c1,state-c1,v1,v2,l1,l2,"a")
                res = min(res,dfs(c1) + dfs(state-c1) + l1+l2 +abs(v1-v2))

            
                    
            return res 
        n = len(lists)
        return dfs((1<<n) -1)

                        

                    


#lists = [[3,10],[1,3,8]]
from input import lists2
re =Solution().minMergeCost(lists2)
print(re)
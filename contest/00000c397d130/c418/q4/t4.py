# https://leetcode.cn/problems/sorted-gcd-pair-queries/description/
# https://leetcode.cn/problems/sorted-gcd-pair-queries/solutions/2940421/er-fen-rong-chi-by-tsreaper-k5yq/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from bisect import bisect_right,insort_left,bisect_left



def getSubListUnderN(n):
    dic =defaultdict(set)
    visited=[[] for _ in range(n+2)]
    dic[1] = set([1])
    for i in range(2,n+1):
        if len(visited[i]):
            a = visited[i][0]
            k = i // a
            s =set(dic[k])
            t =set(s)
            for b in s:
                t.add(b*a) 
            dic[i] = t
            continue
        dic[i]=set([1,i])
        for j in range(i,n+1,i):
            visited[j].append(i)
    return dic

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        pdn = getSubListUnderN(mx+1)
        dic = defaultdict(int)
        c = defaultdict(int)
        for a in nums:
            for b in pdn[a]:
                c[b] +=1
        for i in range(mx,0,-1):
            acc =c[i]*(c[i] -1) //2
            for j in range(2*i, mx+1,i):
                acc -= dic[j]
            dic[i] = acc
        pls =[0] 
        kd= {}
        for i,k in enumerate( sorted(dic.keys())):
            kd[i+1] =k 
            pls.append(pls[-1]+ dic[k])
        #print(pls,kd)
        ret =[]
        for b in queries:
            b+=1
            k = bisect_left(pls,b)
            ret.append(kd[k])
        return ret




re =Solution().gcdValues(nums = [2,3,4], queries = [0,2,2])
print(re)
# https://leetcode.cn/problems/maximum-good-subtree-score/description/
# 因为在求状态merge的时候，不能有重叠状态，所以用bitmask编码，在初始的时候，加入0的状态，可以简化状态merge的分支

from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        mod = 10**9+7 
        n = len(vals)
        g = [[] for _ in range(n)]
        for i,a in enumerate(par):
            if a >=0:
                g[a].append(i)
        ret = 0
        
        def mergeTwo(dic1,dic2):
            dic1kv = list(dic1.items())
            for k,v in dic1kv:
                for k2,v2 in dic2.items():
                    if k&k2 ==0:
                        dic1[k+k2] = max(v+v2,dic1[k+k2])
            return dic1

        
        def isGood(val):
            ls = [a for a in str(val)]
            return len(ls) == len(set(ls))

        def dfs(i):
            nonlocal ret
            dic =defaultdict(int)
            dic[0]=0
            if isGood(vals[i]):
                ls = [int(a) for a in str(vals[i])]
                t = 0 
                for a in ls:
                    t += 1<<int(a)
                dic[t] = vals[i]
            for b in g[i]:
                t1  =dfs(b)
                dic= mergeTwo(dic,t1)
            #print(dic)
            ret += max(dic.values())
            #print(ret)
            return dic

        
        dfs(0)
        return ret %mod
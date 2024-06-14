# https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/?envType=daily-question&envId=2024-06-13

from typing import List, Tuple, Optional

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        dic = {}
        items.sort(reverse= True)
        sm = 0
        cand = []
        for i in range(k):
            a,b = items[i]
            if b not in dic:
                dic[b] =1
            else:
                cand.append(a)
            sm += a 
        cand.sort(reverse= True)
        ss = len(dic.items())
        sm += ss*ss
        #print(sm,ss)
        acc =sm
        for a,b in items[k:]:
            if b not in dic and cand :
                acc+= ss+ss+1+a - cand[-1]
                cand.pop()
                dic[b] =1
                ss +=1
                sm = max(sm,acc)
        return sm
        
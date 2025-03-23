# https://leetcode.cn/problems/minimum-reverse-operations/description/?envType=daily-question&envId=2025-03-20
# L和R是分段折线函数，用max min 合并分段，  -k+1 为无边界的线段函数， k-1-a*2 为边界的时候的函数线段
from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        bd = set(banned)
        ret = [-1]*n 
        sl = [SortedList([]) for _ in range(2)]
        for i in range(n):
            if i not in bd and i != p:
                sl[i%2].add(i)
        cand = [p]
        cnt = 0
        while len(cand):
            tmp = []
            for a in cand:
                ret[a] = cnt 
                slc = sl[(a+k-1)%2]
                # 左右区间确定
                L = max(-k+1,k-1-a*2)
                R = min(1-k+(n-1-a)*2,k-1)
                fidx = slc.bisect_left(a +L)
                rm = []
                while fidx < len(slc) and slc[fidx] <=a +R:
                    
                    rm.append(slc[fidx])
                    fidx +=1
                
                for b in rm:
                    slc.remove(b)
                    tmp.append(b)
            cnt +=1
            #print(cand,tmp)
            cand = tmp
            
        return ret
                
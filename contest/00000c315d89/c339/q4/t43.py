# https://leetcode.cn/contest/weekly-contest-339/problems/minimum-reverse-operations/
#https://leetcode.cn/circle/discuss/K0dVcY/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ret = [-1]*n
        bd = set(banned)
        lss = [SortedList([]) for _ in range(2)]
        for i in range(n):
            if i not in bd and i !=p:
                lss[i%2].add(i)
        st =deque([(p,0)])
        ret[p]= 0
        while st:
            a,cnt = st.popleft()
            ret[a]= cnt
            left =max(-(k-1),k-1-2*a)
            right = min(k-1,-(k-1)+2*(n-1-a))
            ls = lss[(a + k-1)%2]
            idx = ls.bisect_left(a+left)
            toRemove=[]
            while idx<len(ls):
                if ls[idx] >a+right:break
                st.append((ls[idx],cnt+1))
                toRemove.append(ls[idx])
                idx +=1
            for a in toRemove:
                ls.remove(a)
        return ret
        
        





re =Solution().minReverseOperations(n = 5, p = 0, banned = [], k = 4)
print(re)
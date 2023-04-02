from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ret = [-1]*n
        ret[p] =0
        visit={}
        visit[p] =1
        for a in banned:
            visit[a] =1
        cnt =0
        left, right = p,p
        while left != 0  or right != n-1:
            cnt +=1
            ll,rr = left,right
            #print(ret,visit)
            for i in range(max(ll-k+1,0),ll+1):
                if i + k-1>=n:continue
                nexp= i + k-1- (ll-i) 
                #print(nexp,ll,i,"ll")
                if nexp not in visit:
                    ret[nexp] = cnt 
                    visit[nexp] =1
                    left = min(left,nexp)
                    right = max(nexp,right)
            for i in range(max(0,rr-k+1),rr+1):
                if i + k-1>=n:continue
                nexp = i + k -1-(rr-i) 
                #print(nexp,i,rr,"rr")
                if nexp not in visit :
                    ret[nexp] =cnt
                    visit[nexp] =1 
                    right = max(right ,nexp)
                    left = min(left,nexp)
            print(ret,left,right,ll,rr)
            if ll == left and rr ==right:
                break
        return ret
        
        





re =Solution().minReverseOperations(n = 5, p = 0, banned = [], k = 4)
print(re)
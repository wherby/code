from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        dic = defaultdict(list)
        for i in range(m):
            acc =0
            for j in range(n):
                acc = acc*2+ grid[i][j]
            dic[acc].append(i)
        #print(dic)
        if len(dic[0])>0:
            return dic[0]
        
        cnt = [0]*5
        for i in range(32):
            acc =0
            for j in range(5):
                if (1<<j)&i:
                    cnt[j]+= len(dic[i])
        pls=[[] for _ in range(5)]

        for j in range(32):
            acc =0
            for k in range(5):
                if (1<<k)&j:
                    acc +=1
            for i in range(5):
                if (1<<i)&j:
                    pls[i].append((acc,j))
        for i in range(5):
            pls[i].sort()
        #print(dic)

        res = m 
        rm ={}
        while res:
            isB = True
            for i in range(5):
                print(cnt,res,i)
                while cnt[i] > res //2:
                    #print(cnt,res)
                    isB = False
                    if len(pls[i])>0:
                        _,idx = pls[i][-1]
                        if len(dic[idx]) ==0:
                            pls[i].pop()
                        else:
                            rmt = dic[idx].pop()
                            if rmt not in rm:
                                rm[rmt] =1
                                for j in range(5):
                                    if (1<<j) &idx:
                                        cnt[j] -=1
                                res -=1
                                break
            if isB == True:
                break
        if res ==0:
            return []
        ret = []
        for i in range(32):
            for j in dic[i]:
                if j not in rm:
                    ret.append(j)
        ret.sort()
        #print(dic)
        return ret
                    
        



re =Solution().goodSubsetofBinaryMatrix(grid = [[1,1,1,0,0],[0,1,0,1,0],[1,0,0,1,0],[0,1,1,1,0],[1,0,1,0,0],[1,0,0,1,0],[0,1,1,1,1]])
print(re)
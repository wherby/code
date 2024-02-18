from typing import List, Tuple, Optional

from collections import defaultdict,deque
#from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

def isPrime(num):
    if num == 1: return False
    i = 2
    while i * i <= num:   # 可以先求prime list 加速
        if num % i == 0: return False
        i += 1
    return True

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        N= max(m,n)
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        dic = defaultdict(int)

        for i in range(m):
            for j in range(n):
                for dx,dy in dirs:
                    acc = mat[i][j]
                    for k in range(1,N):
                        nx,ny = i + k*dx,j + k*dy 
                        if 0<=nx<m and 0<=ny<n:
                            acc = acc*10+ mat[nx][ny]
                            dic[acc] +=1 
        mx = -1 
        ret =-1 
        for a in dic.keys():
            if isPrime(a):
                if dic[a] > mx:
                    ret = a 
                    mx = dic[a]
                elif dic[a] == mx:
                    ret = max(ret, a )
        return ret





re =Solution().mostFrequentPrime([[1,7,2,6,6,2],[4,7,1,3,2,3],[8,7,7,4,5,3],[9,8,8,2,7,9]])
print(re)
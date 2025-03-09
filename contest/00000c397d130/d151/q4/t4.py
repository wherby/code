from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf
from math import factorial

# def get_kth_permutation(N, K):
    

#     # 初始化数字列表
#     nums = list(range(1, N + 1))
#     result = []

#     # 将 K 转换为阶乘数系统
#     K -= 1  # 转换为从 0 开始计数
#     for i in range(N - 1, -1, -1):
#         fact = factorial(i)
#         index = K // fact
#         result.append(str(nums.pop(index)))
#         K %= fact

#     return ''.join(result)

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        if n ==1:
            if k == 1:
                return [1]
            return []
        ret =[-1]*n
        k =k-1
        def findNext(k,fst,lst,i):
            n1 = len(fst)
            n2 = len(lst)
            idx = k //(factorial(n1-1)*factorial(n2))
            ret[i] = fst[idx]
            fst.pop(idx)
            k = k%(factorial(n1-1)*factorial(n2))
            if i+1<n:
                findNext(k,lst,fst,i+1)

        if n%2 ==0:
            if k >= ((factorial(n//2-1))*(factorial(n//2)))*n:
                return  []
            ls = [i for i in range(1,n+1)]
            idx = k //((factorial(n//2-1))*(factorial(n//2)))
            #print(idx,ls)
            ret[0] = ls[idx]
            ls.pop(idx)
            od = [i for i in ls if i%2 ==1]
            ev = [i for i in ls if i%2 ==0]
            k = k %((factorial(n//2-1))*(factorial(n//2)))
            #print(ret)
            if ret[0]%2 ==0:
                findNext(k,od,ev,1)
            else:
                findNext(k,ev,od,1)
        else:
            ls = [i for i in range(1,n+1)]
            od = [i for i in ls if i%2 ==1]
            ev = [i for i in ls if i%2 ==0]
            idx = k //((factorial(n//2))*(factorial(n//2)))
            if idx > n//2:
                return []
            
            ret[0] = od[idx]
            od.pop(idx)
            k= k %((factorial(n//2))*(factorial(n//2)))
            #print(idx,k,((factorial(n//2))*(factorial(n//2))))
            findNext(k,ev,od,1)
        return ret






re =Solution().permute(n = 6, k = 71)
print(re)
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


from math import sqrt

def get_prime_factor(num):
    # 质因数分解
    res = []
    for i in range(2, int(sqrt(num)) + 1):
        cnt = 0
        while num % i == 0:
            num //= i
            cnt += 1
        if cnt:
            res.append([i, cnt])
        if i > num:
            break
    if num != 1 or not res:
        res.append([num, 1])
    return res

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        pls = get_prime_factor(t)
        acc =0
        dic = defaultdict(int)
        for a,b in pls:
            if a >9:
                return -1
            acc +=b
            dic[a] = b
        
        n = len(num)
        while acc>n:
            if dic[3]>=2:
                dic[3]-=2
                dic[9] +=1
                acc-=1
            elif dic[4]>=1 and dic[2]>=1:
                dic[4] -=1
                dic[2] -=1
                dic[8] +=1
                acc-=1
            elif dic[2]>=1 and dic[3]>=1:
                dic[3] -=1
                dic[2] -=1
                dic[6] +=1
                acc-=1
            elif dic[2] >=2:
                dic[2] -=2
                dic[4] +=1
                acc-=1
            else:
                break
        ls = []
        for i in range(10):
            ls.extend([str(i)]*dic[i])
        print(acc,ls)
        if acc >n:
            
            return "".join(ls)
        
        elif acc<=n:
            ret =[]
            for i in range(n):
                if i+acc+1>=n:
                    break
                ret.append(num[i])
                t = int(num[i])
                if t == 9:
                    if dic[3]>=2:
                        dic[3] -=2
                        acc -=2
                    elif dic[9]>=1:
                        dic[9] -=1
                        acc -=1
                elif t ==8:
                    if dic[2] >=3:
                        dic[2] -=3
                        acc-=3
                    elif dic[2] >=1 and dic[4] >=1:
                        dic[2] -=1
                        dic[4] -=1
                        acc-=2
                    elif dic[8]>=1:
                        dic[8] -=1
                        acc-=1
                elif t == 6:
                    if dic[2] >=1 and dic[3] >=1:
                        dic[2] -=1
                        dic[3] -=1
                        acc -=2
                    elif dic[t] >=1:
                        dic[t] -=1
                        acc-=1
                elif t ==4:
                    if dic[2] >=2:
                        dic[2] -=2
                        acc-=2
                    elif dic[4] >=1:
                        dic[4] -=1
                        acc -=1
                elif dic[t]>=1:
                    dic[t] -=1
                    acc-=1
            ls  =[]
            if acc ==0:
                return "".join(ret)
            for i in range(10):
                ls.extend([int(i)] * dic[i])
            print(ret)
            

        

#222334
#23344
#22346
#22249
#22338





re =Solution().smallestNumber(num = "1234", t = 256)
print(re)
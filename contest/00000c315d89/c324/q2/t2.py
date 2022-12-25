from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
def get_prime(n):
    cnt =0
    prime=[0]*(n+2)
    st = [False] *(n+2)

    for i in range(2,n+1):
        if not st[i]:
            prime[cnt] =i
            cnt +=1
            
        j = 0
        while prime[j] <= n/i:
            st[prime[j]*i] =True
            if i % prime[j] ==0:
                break
            j +=1
    return prime[:cnt]

class Solution:
    def smallestValue(self, n: int) -> int:
        pTo10= get_prime(10**5+2)
        #print(pTo10[:5])
        pls =set(pTo10)
        def verify(n):
            g =n
            if n in pls:
                return n 
            acc =0
            
            for a in pls :
                while a <=n and n%a ==0:
                    acc +=a 
                    n = n//a 
            return verify(acc) if g!=acc else g
        return verify(n)




re =Solution().smallestValue(4)
print(re)
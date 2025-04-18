from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        #if k ==1 :return 1
        prime = {'2', '3', '5', '7'}
        if s[0] not in prime or s[-1] in prime:
            return 0
        if k ==1:return 1
        n = len(s)
        cut =[]
        for i in range(1,n-1):
            if i+1>=minLength and n-i-1>= minLength and  s[i] not in prime and s[i+1] in prime:
                cut.append(i)
        #print(cut,n)
        m = len(cut)
        dp= [[0]*m for _ in range(k)]
        for i,c in enumerate(cut):
            if c +1 >= minLength and n-c-1 >= minLength:
                #print(n-c-1,c)
                dp[0][i] =1
        mod = 10**9+7
        for i in range(1,k):
            acc =0
            left =0
            for j in range(m):
                while left<m and   cut[j]-cut[left]>=minLength :
                    acc +=dp[i-1][left]
                    left +=1
                dp[i][j]+=acc
                dp[i][j] %= mod
        #print(dp,k)
        
        return sum(dp[k-2])%mod 



re =Solution().beautifulPartitions("7828745959293979512154292859512679792934793978763959293424767156567959567139745429797456597826382958243929397958285978247839397971587976762854797874585179263974393179217971597439267159597174393871767671292159395179582476397626797436717821212956297951545621597478797459797974347929767971385629717134587854787636597824217679245426583626717679797958517626567429792659582971795878397428782871215676787159382674265429392651743151717658343676212659747676797859795456262139245436742471292959793176587124217926395829793976592938382158793878715456262659342951587126282478795679742174345154397679717674383971212978743478397156265928597621213829742426762674795929793878767421313671297124717679345676512879783159367478347159767959787951765934387429792978787429793459717439382626543179787456343978783851247174765979715458765129765629362426797954342859317871587979395851762979362151397659795951715936347978792154397971547624247474513859563976397479295879515959293159367179765876787426317174315936763976597179595826",500,1)
print(re)
re =Solution().beautifulPartitions(s = "23542185131", k = 3, minLength = 2)
print(re)
re =Solution().beautifulPartitions(s = "3312958", k = 1, minLength = 1)
print(re)
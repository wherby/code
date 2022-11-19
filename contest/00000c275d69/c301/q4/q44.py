
from functools import cache

from collections import defaultdict,deque
def getSubListUnderN(n):
    dic =defaultdict(set)
    visited=[[] for _ in range(n+2)]
    dic[1] = set([1])
    for i in range(2,n+1):
        if len(visited[i]):
            a = visited[i][0]
            k = i // a
            s =set(dic[k])
            t =set(s)
            for b in s:
                t.add(b*a) 
            dic[i] = t
            continue
        dic[i]=set([1,i])
        for j in range(i,n+1,i):
            visited[j].append(i)
    return dic
class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        sm = 0
        dic = getSubListUnderN(maxValue)
        #print(dic)
        @cache
        def getMem(n,mx):
            if n <=1 or mx ==1:
                return 1
            ret =0
            for i in dic[mx]:
                ret += getMem(n//2,mx//i)*getMem(n-n//2,i)
                #print(getMem(n-1,mx//i),n-1,mx//i,ret)
            return ret 
        mod = 10**9+7
        for i in range(1,maxValue+1):
            sm += getMem(n,i)%mod
        return sm %mod

#re =Solution().idealArrays(n = 5878, maxValue = 2900)
#re =Solution().idealArrays(n = 37, maxValue = 71)
re = Solution().idealArrays(n = 2, maxValue = 5)
re = Solution().idealArrays(n = 10000, maxValue = 9999)
print(re)
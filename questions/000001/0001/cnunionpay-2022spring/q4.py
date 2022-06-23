import collections
import itertools
class Solution(object):
    def coopDevelop(self, skills):
        """
        :type skills: List[List[int]]
        :rtype: int
        """
        def myHash(s):
            res = 0
            for x in s:
                res <<=10
                res +=x
            return res
        c = collections.Counter()
        n = len(skills)
        for i in range(n):
            skills[i].sort()
        for i in range(n):
            c[myHash(skills[i])] +=1
        cnt =0 
        for key in c:
            cnt += c[key] * (c[key] -1) //2
        for i in range(n):
            for j in range(1,len(skills[i])):
                for a in itertools.combinations(skills[i],j):
                    cnt += c[myHash(a)]
        mod = 10 **9+7
        return ((n*(n-1))//2 -cnt)%mod
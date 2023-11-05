import itertools
import functools
MODULUS=10**9+7

@functools.cache
def ok2(s1, s2):
    for i in range(len(s1)):
        if s1[i] == s2[i]: return False
    return True
class Solution(object):
    def ok1(self, seq):
        for i in range(self.m-1):
            if seq[i] == seq[i+1]: return False
        return True

    @functools.lru_cache(None) 
    def ans(self, n, prev):
        if n == 0: return 1
        ret = 0
        for s in self.states: 
            if ok2(s, prev):
                ret += self.ans(n-1,s)
                ret %= MODULUS
        return ret % MODULUS
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
    def colorTheGrid(self, m: int, n: int) -> int:
        self.m = m
        self.states = []

        for seq in itertools.product([0,1,2], repeat=m):
            if self.ok1(seq):
                self.states += [seq]
        #print(self.states)
        return self.ans(n, (-1,)*m)
            

a =Solution().colorTheGrid(1,1)
print(a)
a= Solution().colorTheGrid(1,2)
print(a)
a =Solution().colorTheGrid(5,5)
print(a)
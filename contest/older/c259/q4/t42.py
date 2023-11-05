import collections
import itertools
class Solution:
    def isSubsequence(self,s,t):
        t=iter(t)
        return all(c in t for c in s)
    
    def longestSubsequenceRepeatedK(self, s, k):
        hot = "".join(el *(freq //k) for el,freq in collections.Counter(s).items())

        comb =set()
        for l in range(len(hot) +1):
            for cand in itertools.combinations(hot,l):
                for perm in itertools.permutations(cand):
                    comb.add("".join(perm))
        
        comb = sorted(comb,key=lambda x: (len(x),x),reverse=True)

        for c in comb:
            if self.isSubsequence(c *k,s):
                return c

re =Solution().longestSubsequenceRepeatedK("bbabbabbbbabaababab",3)
print(re)
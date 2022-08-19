
            
import itertools


class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        def verify(ls):
            for i,a in enumerate(pattern):
                if a =="I" and ls[i]>ls[i+1]:
                    return False
                elif a == "D" and ls[i]<ls[i+1]:
                    return False
            return True
        n = len(pattern)
        ls = [i for i in range(1,n+2)]
        for tls in itertools.permutations(ls):
            if verify(tls):
                return "".join([str(a) for a in tls])

re =Solution().smallestNumber("IIIDIDDD")
print(re)
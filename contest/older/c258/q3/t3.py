import functools
class Solution:
    def maxProduct(self, s: str) -> int:
        @functools.lru_cache(None) 
        def isPalind(mask):
            t = ""
            for i in range(nc):
                if mask & 1 <<i  !=0:
                    t += s[i]
            n1 = len(t)
            for i in range(n1):
                if t[i] != t[n1-1-i]:
                    return 0
            return len(t)
        nc = len(s)
        n = 1<<nc
        mx=0
        for i in range(n):
            t1 = isPalind(i)
            if t1 ==0:
                continue
            for j in range(n):
                if i &j ==0:
                    t2 = isPalind(j)
                    #print(i,j,t1,t2)
                    mx = max(mx, t1 *t2)
        return mx


s = "accbcaxxcxx"
a=Solution().maxProduct(s)
print(a)
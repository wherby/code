class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        g =[[-1] for _ in range(26)]
        for i,a in enumerate(s):
            k = ord(a) -ord('a')
            g[k].append(i)
        acc =0
        for i in range(26):
            g[i].append(n)
        for i in range(26):
            ls =g[i]
            for k in range(1,len(ls)-1):
                j = ls[k]
                jn=ls[k+1]
                jp = ls[k-1]
                acc += (j-jp)*(n-j)
        return acc
        

re =Solution().appealSum("code")
print(re)
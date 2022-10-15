# https://leetcode.cn/submissions/detail/372863477/

# https://leetcode.cn/problems/distinct-subsequences-ii/solution/bu-tong-de-zi-xu-lie-ii-by-leetcode-solu-k2h5/

class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        lst =[-1]*26
        f = [1] * n 
        mod = 10**9+7
        for i,a in enumerate(s):
            for j in range(26):
                if lst[j] != -1:
                    f[i] += f[lst[j]] 
                    f[i] %= mod
            lst[ord(a) - ord('a')] =i 
        acc = 0 
        for i in range(26):
            if lst[i] != -1:
                acc += f[lst[i]]
                acc %=mod 
        return acc
    
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ls= [0]*26
        for a in s:
            k = ord(a) -ord('a')
            total = 1 + sum(ls)
            ls[k] = total
        mod = 10**9+7
        return sum(ls)%mod

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ls= [0]*26
        total =0 
        mod =10**9+7
        for a in s :
            k = ord(a)-ord("a")
            ls[k],total= (total +1)%mod,(total*2+1 -ls[k])%mod
        return total
class Solution(object):
    def makeStringSorted(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ls =[0]*n
        ordls =[0]*26
        for i in range(n):
            k = ord(s[i]) -ord('a')
            ls[i] = k
            ordls[k] +=1
        mod = 10**9 +7

        factorial = [1]*3001
        for i in range(1,3001):
            factorial[i] = factorial[i-1]*i %mod
        def inv2(x):
            s= 1
            while x >1:
                s= s*(mod-mod//x)%mod
                x = mod%x
            return s
        ret = 0
        #print(ordls,ls)
        for i in range(n):
            cnt =0
            for k in range(ls[i]):
                cnt += ordls[k]
            ans = factorial[n-i-1] %mod
            for k in range(26):
                ans = ans * inv2(factorial[ordls[k]]) %mod
            
            ret =(ret + cnt *ans % mod)%mod
            #print(ret)
            ordls[ls[i]] -=1
        return ret


#dp[0] =0
#dp[1] =1
#dp[2] = 

# dabc =>cabd=>badc =>bacd=>adcb =>abcd
# cba => abc

re = Solution().makeStringSorted("leetcodeleetcodeleetcode")
print(re)
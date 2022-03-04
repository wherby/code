class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        m = len(n)
        cand = [10**m +1 , 10**(m-1)-1]
        hf = (m+1)//2
        hfit = int(n[:hf])
        for a in range(hfit-1,hfit+2):
            ls = [t for t in n]
            pa = [m for m in str(a)]
            for i,x in enumerate(pa):
                if i < m:
                    ls[i]=pa[i]
                    ls[m-1-i] = pa[i]
            cand.append(int("".join(ls)))
        ans = ""
        mx = cand[0]
        for c in cand:
            if abs(c-int(n))< mx and c != int(n):
                mx = abs(c-int(n))
                ans = str(c)
        return ans


re = Solution().nearestPalindromic("9")
print(re)

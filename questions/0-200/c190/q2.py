class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set(["a", "e", "i", "o", "u"])
        n= len(s)
        ls = [0]*(n+1)
        for i,a in enumerate(s):
            ls[i+1] = ls[i] +(a in vowels)
        mx = 0
        for i in range(k,n+1):
            j = i-k
            if j <n+1:
                mx = max(mx, ls[i] -ls[j])
        return mx
                

            

re = Solution().maxVowels(s = "abciiidef", k = 3)
print(re)
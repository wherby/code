# https://leetcode.cn/problems/count-substrings-that-differ-by-one-character/
class Solution(object):
    def countSubstrings(self, s, t):
        m,n = len(s),len(t)
        cnt = 0 
        for i in range(m):
            for j in range(n):
                diff = 0 
                k = 0 
                while diff <2 and i+k <m and j+k <n:
                    if s[i+k] != t[j+k]:
                        diff +=1
                    if diff ==1:
                        cnt +=1
                    k +=1
        return cnt




re = Solution().countSubstrings(s = "aba", t = "baba")
print(re)

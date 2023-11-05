import functools
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @functools.lru_cache(None)
        def lcs(str1,str2):
            if not str1 or not str2:
                return ""
            if str1[0] == str2[0]:
                return str1[0] + lcs(str1[1:],str2[1:])
            else:
                return  max(lcs(str1,str2[1:]),lcs(str1[1:],str2),key=len)
        res =""
        for c in lcs(str1,str2):
            (front1,str1),(front2,str2) =str1.split(c,1),str2.split(c,1)
            res = res+ front1 + front2 + c 
        return res + str1 + str2
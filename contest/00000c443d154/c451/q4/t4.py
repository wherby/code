# https://leetcode.cn/contest/weekly-contest-451/problems/lexicographically-smallest-string-after-adjacent-removals/description/
from typing import List, Tuple, Optional

from functools import cache


class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        
        def good(i,j):
            if abs(ord(s[i]) - ord(s[j])) ==1 or abs(ord(s[i])-ord(s[j])) ==25:
                return True

        @cache
        def isGood(i,j):
            if j-i %2 ==0:
                return False
            if i >j :
                return True
            if good(i,j) and isGood(i+1,j-1):
                return True
            for k in range(i+1,j,2):
                if isGood(i,k) and isGood(k+1,j):
                    return True
            return False
        n = len(s)
        @cache
        def dfs(i):
            if  i == n:
                return "" 
            ret = s[i] + dfs(i+1)
            for j in range(i+1,n):
                if isGood(i,j):
                    t = dfs(j+1)
                    if ret >t:
                        ret  =t 
            return ret
        return dfs(0)




s = "rsqsnsooqqmsmpnrronqonmrnmqpoqnroqrrmppqnmmpopononnsomrsmmmnsrnpropsomqomqpsnsmqsnnopprmmnsnnnqqrroornnrosnrmsnnqprommsrrpnqsmoqqmoomspmqnpnsrmnmoonrromnrssmnprrprssssssrmpmmrprommsooommqsrsrnoomospmmmqnsqrmqrprsqnpspnrmmnp"
re =Solution().lexicographicallySmallestString(s)
print(re)
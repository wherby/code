# https://leetcode.cn/problems/find-the-lexicographically-smallest-valid-sequence/description/?envType=daily-question&envId=2026-08-08

from typing import List, Tuple, Optional
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n= len(word1)
        m = len(word2)
    

        def getDP(w1,w2):
            cur = 0
            ret = [n]*m
            for i,a in enumerate(w1):
                if cur ==m:
                    return ret
                if a ==w2[cur]:
                    ret[cur] = i
                    cur +=1
            return ret 
        dp2= getDP(word1[::-1],word2[::-1])

        ans = []
        cur = 0
        used = False   
        for i,a in enumerate(word1):
            if cur ==m:
                return ans
            if a == word2[cur]:
                ans.append(i)
                cur +=1
            else:
                if used == False and (m-2-cur <0 or dp2[m-cur-2] + i+2 <= n)   :
                    used = True
                    cur +=1
                    ans.append(i)
        return ans if len(ans) == m else []
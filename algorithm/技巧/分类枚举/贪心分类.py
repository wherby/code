# https://leetcode.cn/problems/two-letter-card-game/solutions/3768070/mei-ju-jie-lun-pythonjavacgo-by-endlessc-zbnv/
# 利用贪心分类，先解决最不能匹配的额， 然后贪心匹配之后丢弃不能使用的，再分情况讨论
#

from typing import List, Tuple, Optional

import math
INF  = math.inf

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        dp = [[0]*26 for _ in range(3)]
        for card in cards:
            a,b = card
            if a ==x and b ==x:
                dp[0][0]+=1
            elif a ==x:
                c= ord(b) - ord("a")
                dp[1][c]+=1
            elif b == x:
                c = ord(a) - ord("a")
                dp[2][c]+=1
        dp2 = [0]*3
        dp2[0] = dp[0][0]
        cnt = 0
        #print(dp)
        
        for i in range(1,3):
            sm = sum(dp[i])
            mx = max(dp[i])
            if mx *2 > sm:
                t = min(dp2[0],mx-(sm-mx))
                
                dp2[0] -=t
                cnt +=t
                dp2[i]= ((sm-mx) )*2
            else:
                dp2[i]= sm 
            if dp2[i]%2 ==1 and dp2[0]:
                cnt +=1
                dp2[0] -=1
                dp2[i] -=1
            if dp2[i]%2 == 1:
                dp2[i] -=1

        if dp2[1]+dp2[2] >= dp2[0]:
            return cnt + sum(dp2)//2
        else:
            return sum(dp2[1:3]) +cnt




re =Solution().score(cards =["ab","aa","ab","bc","cc","bc","bb","ac","bc","bc","aa","aa","ba","bc","cb","ba","ac","bb","cb","ac","cb","cb","ba","bc","ca","ba","bb","cc","cc","ca","ab","bb","bc","ba","ac","bc","ac","ac","bc","bb","bc","ac","bc","aa","ba","cc","ac","bb","ba","bb"],x = "b")
print(re)

re =Solution().score(["eb","he","ce","gc","cd","ca","gj","ji","hc","gb","fi","gg","hb","aj","hd","ba","ef","aa","ef","jc","ff","dg","jd","dj","aa","fb","bc","gc","cf","af","bd","fd","hf","jg","ha","db","cd","ij","bi","ga","eh","jf","ha","af","hc","dj","fb","fc","de","ej"],"c")

print(re)
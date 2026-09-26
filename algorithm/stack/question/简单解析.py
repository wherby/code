# https://leetcode.cn/problems/evaluate-the-bracket-pairs-of-a-string/description/?envType=daily-question&envId=2026-09-26

from typing import List, Tuple, Optional
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dic = {}
        for k,v in knowledge:
            dic[k]=v 
        res = ""
        cur = ""
        for a in s:
            if a =="(":
                res += cur 
                cur =""
            elif a ==")":
                if cur not in dic:
                    res +="?"
                else:
                    res +=dic[cur]
                cur = ""
            else:
                cur +=a 
        return res + cur
# https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/submissions/614296366/?envType=daily-question&envId=2025-03-23
# 前后verify
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        def verify(s,locked,b):
            acc =0
            nuse = 0
            for a,l in zip(s,locked):
                if l =="0":
                    nuse +=1
                else:
                    if a == b:
                        acc -=1
                        while acc <0:
                            if nuse >0:
                                nuse -=1
                                acc +=1
                            else:
                                return False
                    else:
                        acc +=1
                #print(nuse,acc)
            #print(nuse,acc)
            return nuse >=acc and (nuse -acc) %2 ==0
        return verify(s,locked,")") and verify(s[::-1],locked[::-1],"(")

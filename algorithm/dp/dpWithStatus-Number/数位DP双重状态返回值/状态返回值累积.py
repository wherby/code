# https://leetcode.cn/problems/total-waviness-of-numbers-in-range-i/description/?envType=daily-question&envId=2026-06-04
# 使用状态返回值累积的方式可以不使用双重返回值

from functools import cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def dp(a):
            s = str(a)

            @cache 
            def f(i, is_limit,is_num,state,lastv,acc):
                if i ==len(s):
                    return acc if is_num else 0
                
                res = 0
                if not is_num:
                    res= f(i+1,False,False,state,lastv,acc)
                up = int(s[i]) if is_limit else 9 
                for d in range(0 if is_num else 1, up+1):
                    newLimit = is_limit and d ==up
                    if state==-1:
                        res += f(i+1,newLimit,True,0,d,acc)
                    else:
                        if d == lastv:
                            res += f(i+1,newLimit,True,0,d,acc)
                        elif d > lastv:
                            res += f(i+1,newLimit,True,1,d,acc +int(state == 2))
                        else:
                            res += f(i+1,newLimit,True,2,d,acc +int(state ==1))

                return res
            return f(0,True,False,-1,0,0)
        return dp(num2) -dp(num1-1)
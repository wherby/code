# https://leetcode.cn/problems/total-waviness-of-numbers-in-range-i/description/?envType=daily-question&envId=2026-06-04
# 在DP的时候，当前状态的贡献值需要 乘上当前状态的后续状态数量
# 所以DP 返回的是 双重返回值 （后续状态的数量，后续子状态的贡献）
# 状态转移的时候 sacc =sacc + hasNew*res[0] + res[1]  需要累加后续状态的贡献 和当前贡献和后续状态数量的乘积

from functools import cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def dp(a):
            s = str(a)
            n = len(s)

            @cache 
            def f(i, is_limit,is_num,state,lastv):
                if i ==len(s):
                    return (1,0) if is_num else (0,0)
                
                nacc,sacc = 0,0
                if not is_num:
                    nacc,sacc = f(i+1,False,False,state,lastv)
                up = int(s[i]) if is_limit else 9 
                for d in range(0 if is_num else 1, up+1):
                    newLimit = is_limit and d ==up
                    hasNew = 0
                    if state==-1:
                        res = f(i+1,newLimit,True,0,d)
                    else:
                        if d == lastv:
                            res = f(i+1,newLimit,True,0,d)
                        elif d > lastv:
                            res = f(i+1,newLimit,True,1,d) 
                            hasNew = int(state == 2)
                        else:
                            res = f(i+1,newLimit,True,2,d) 
                            hasNew = int(state ==1)
                    sacc =sacc + hasNew*res[0] + res[1]
                    nacc = nacc + res[0]
                return (nacc,sacc)
            return f(0,True,False,-1,0)[1]
        return dp(num2) -dp(num1-1)
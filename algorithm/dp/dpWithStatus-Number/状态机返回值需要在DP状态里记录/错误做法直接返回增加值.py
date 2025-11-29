# 状态生成的值直接返回没有记录在状态里，所以是错误的
# DP 常见错误
# 这种写法的+1只会影响当前分支， 不影响后续递归，但是这里的增加值是和状态一起的，所以后续的递归也会有这个+1的影响
from typing import List, Tuple, Optional

from functools import cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        @cache 
        def f(i,is_limit,is_num,s,state,last):
            if i == len(s):
                return 0
            res = 0
            if not is_num:
                res = f(i+1,False,False,s,-1,-1)
            up = int(s[i]) if is_limit else 9 
            for d in range(0 if is_num else 1, up +1):
                if state == -1:
                    res += f(i+1,is_limit and d == up, True,s,0,d)
                else:
                    if d >last:
                        if state ==2:
                            res += f(i+1,is_limit and d == up, True,s,1,d) +1
                        else:
                            res += f(i+1,is_limit and d == up, True,s,1,d)
                    elif d < last:
                        if state ==1:
                            res += f(i+1,is_limit and d == up, True,s,2,d) +1
                        else:
                            res += f(i+1,is_limit and d == up, True,s,2,d)
                    elif d== last:
                        res += f(i+1,is_limit and d == up, True,s,0,d)
            return res 
        a1 = f(0,True,False,str(num2),-1,-1)
        a2 = f(0,True,False,str(num1-1),-1,-1)
        #@print(a1,a2)
        return a1-a2
            




re =Solution().totalWaviness(4848,4848)
print(re)
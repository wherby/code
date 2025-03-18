# https://leetcode.cn/contest/weekly-contest-441/problems/count-beautiful-numbers/description/

from functools import cache

class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:

        def count(num):
            s  = str(num)
            n = len(s)

            @cache
            def f(i,is_limit,is_num,acc,sm):
                if i ==len(s):
                    return int(is_num and acc%sm ==0)
                res =0
                if not is_num:
                    res = f(i+1,False,False,1,0) ##计算 0-9，10-99，100-999，1000-9999
                up = int(s[i]) if is_limit else 9
                for d in range(0 if is_num else 1, up +1):
                    res += f(i+1,is_limit and d ==up, True,acc*d,sm+d)
                return res
            return f(0,True,False,1,0)
        return count(r) -count(l-1)





re =Solution().beautifulNumbers(10,200000)
print(re)
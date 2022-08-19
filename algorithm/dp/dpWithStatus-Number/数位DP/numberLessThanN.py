# https://leetcode.cn/contest/weekly-contest-306/problems/count-special-integers/
# https://leetcode.cn/problems/count-special-integers/solution/shu-wei-dp-mo-ban-by-endlesscheng-xtgx/

from functools import cache

#提供一个一般化的数位 DP 模板。
#将 n 转换成字符串 s，定义 f(i,mask,isLimit,isNum) 表示从构造 n 从高到低第 i 位及其之后位的方案数，
# 其余参数的含义为：

#要选的数字不能在 mask 集合中。
#isLimit 表示当前是否受到了 n 的约束。若为真，则第 i 位填入的数字至多为 s[i]，否则可以是 9。
#isNum 表示 i 前面的位数是否填了数字。若为假，则当前位可以跳过（不填数字），或者要填入的数字至少为 1；若为真，则要填入的数字可以从 0 开始。


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i,mask,is_limit,is_num):
            if i ==len(s):
                return int(is_num)
            res =0
            if not is_num:
                res = f(i+1,mask,False,False) ##计算 0-9，10-99，100-999，1000-9999
            up = int(s[i]) if is_limit else 9
            for d in range(0 if is_num else 1, up +1):
                if mask>>d & 1 ==0:
                    res += f(i+1,mask |(1<<d),is_limit and d ==up, True)
            return res
        return f(0,0,True,False)
    
re =Solution().countSpecialNumbers(20)
print(re)
# https://leetcode.cn/contest/biweekly-contest-111/problems/number-of-beautiful-integers-in-the-range/

from functools import cache

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        @cache
        def f(i: int, is_limit: bool, is_num: int,s,ba,acc) -> int:
            n = len(s)
            if i == len(s): 
                return  is_num and ba ==0 and acc%k ==0
            res = 0
            if not is_num:  # 前面不填数字，那么可以跳过当前数位，也不填数字
                # is_limit 改为 False，因为没有填数字，位数都比 n 要短，自然不会受到 n 的约束
                # is_num 仍然为 False，因为没有填任何数字
                res = f(i + 1, False, 0,s,ba,acc)
            up = int(s[i]) if is_limit else 9  # 根据是否受到约束，决定可以填的数字的上限
            # 注意：对于一般的题目而言，如果此时 is_num 为 False，则必须从 1 开始枚举，由于本题 digits 没有 0，所以无需处理这种情况
            for d in range(0 if is_num else 1, up +1):  # 枚举要填入的数字 d
                aa = d *(10**(n-1-i)) %k
                if d %2 ==0:
                    res += f(i+1,is_limit and d == up, is_num+d,s,ba +1,acc+aa)
                else:
                    res += f(i+1,is_limit and d == up, is_num+d,s,ba -1,acc+aa)
            return res
        f1 = f(0,True,0,str(high),0,0)
        f2 = f(0,True,0,str(low-1),0,0)
        return f1-f2
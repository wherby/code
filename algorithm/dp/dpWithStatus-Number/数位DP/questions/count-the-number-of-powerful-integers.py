# https://leetcode.cn/problems/count-the-number-of-powerful-integers/?envType=daily-question&envId=2025-04-10
from functools import cache
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s1: str) -> int:
        m= len(s1)
        @cache
        def f(i: int, is_limit: bool, is_num: int,s:str) -> int:
            if i > len(s)-len(s1):
                return 0 
            if i == len(s) - len(s1): 
                if is_limit and int(s[-m:])< int(s1):
                    #print(is_limit,s,s[-m:])
                    return 0
                return  int(s)>=int(s1) 
            res = 0
            if not is_num:  # 前面不填数字，那么可以跳过当前数位，也不填数字
                # is_limit 改为 False，因为没有填数字，位数都比 n 要短，自然不会受到 n 的约束
                # is_num 仍然为 False，因为没有填任何数字
                res = f(i + 1, False, 0,s)
            up = int(s[i]) if is_limit else 9  # 根据是否受到约束，决定可以填的数字的上限
            # 注意：对于一般的题目而言，如果此时 is_num 为 False，则必须从 1 开始枚举，由于本题 digits 没有 0，所以无需处理这种情况
            for d in range(0 if is_num else 1, up +1):  # 枚举要填入的数字 d
                if d > up or d >limit: break  # d 超过上限，由于 digits 是有序的，后面的 d 都会超过上限，故退出循环
                # is_limit：如果当前受到 n 的约束，且填的数字等于上限，那么后面仍然会受到 n 的约束
                # is_num 为 True，因为填了数字
                res += f(i + 1, is_limit and d == up, is_num+d,s)
            return res
        return f(0,True,0,str(finish)) - f(0,True,0,str(start-1))
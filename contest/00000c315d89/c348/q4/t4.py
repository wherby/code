# https://leetcode.cn/contest/weekly-contest-348/problems/count-of-integers/
# 数位DP 
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        
        @cache
        def f(i: int, is_limit: bool, is_num: int,num) -> int:
            nonlocal s
            if i == len(s): 
                return  is_num>=min_sum and is_num<= max_sum  # 如果填了数字，则为 1 种合法方案
            res = 0
            if not is_num:  # 前面不填数字，那么可以跳过当前数位，也不填数字
                # is_limit 改为 False，因为没有填数字，位数都比 n 要短，自然不会受到 n 的约束
                # is_num 仍然为 False，因为没有填任何数字
                res = f(i + 1, False, 0,num)
            up = int(s[i]) if is_limit else 9  # 根据是否受到约束，决定可以填的数字的上限
            # 注意：对于一般的题目而言，如果此时 is_num 为 False，则必须从 1 开始枚举，由于本题 digits 没有 0，所以无需处理这种情况
            for d in range(0 if is_num else 1, up +1):  # 枚举要填入的数字 d
                if d > up: break  # d 超过上限，由于 digits 是有序的，后面的 d 都会超过上限，故退出循环
                # is_limit：如果当前受到 n 的约束，且填的数字等于上限，那么后面仍然会受到 n 的约束
                # is_num 为 True，因为填了数字
                res += f(i + 1, is_limit and d == up, is_num+d,num)
            return res
        s = [a for a in str(int(num1)-1)]
        a1 = f(0,True,0,num1)
        #print(a1)
        s =[a for a in num2]
        a2 = f(0,True,0,num2)
        #print(a2)
        mod = 10**9+7
        return (a2 -a1)%mod





re =Solution().count( "1", "12", 1, 8)
print(re)
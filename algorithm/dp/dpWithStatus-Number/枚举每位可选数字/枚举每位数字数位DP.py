# https://leetcode.com/contest/weekly-contest-470/problems/count-no-zero-pairs-that-sum-to-n/submissions/1791741987/
# 因为限制了a,b各个位置上不为0， 所以只用一个数字遍历的话逻辑麻烦，所以需要枚举两个不同数字，找到符合条件的情况进行DP
from functools import cache


class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = str(n)
        m = len(s)

        @cache
        def f(i,c,za,zb):
            if i ==m:
                return 1 if c ==0 and (za ==False and zb ==False) else 0
            res =0
            d= int(s[i]) +10*c
            fa = 0 if za else 1 
            fb = 0 if zb else 1
            for nc in range(2):
                for a in range(fa,10):
                    for b in range(fb,10):
                        if (a+b+nc) ==d:
                            res += f(i+1,nc,za and a ==0 ,zb and b==0)
            return res

                    

        return f(0,0,True,True)

re =Solution().countNoZeroPairs(11)
print(re)
# https://codeforces.com/gym/104574/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0304/solution/cf104574e.md
# 打表发现操作循环规律，8次完美洗牌之后就回到原点了


import init_setting
from lib.cflibs import *
def main(): 
    nums = LII()
    
    for _ in range(8):
        nnums = []
        for i in range(26):
            nnums.append(nums[i])
            nnums.append(nums[i + 26])
        nums = nnums
        
        flg = True
        for i in range(26, 52):
            if nums[i] == 1:
                flg = False
        
        if flg: exit(print('YES'))
    
    print('NO')
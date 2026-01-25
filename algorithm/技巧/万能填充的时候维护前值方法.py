# https://codeforces.com/gym/103185/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0122/solution/cf103815b.md
# 在万能填充的时候，需要维护上一个有效的真正值，需要维护一个pos 表示上一个真正有效值的index，作为趋势的比较
# 在求从当前点到后能最多增长或者减少的长度，需要从后到前比较，这样得到的长度才是当前值的长度
# inc_length 这里定义的是在当前点 非递增数组的最长长度，和字面意思相反
# 万能填充的前后缀求值技巧

import init_setting
from cflibs import *

def main(): 
    n = II()
    nums = LII()
    
    inc_length = [1] * n
    pos = -1
    
    for i in range(n - 1, -1, -1):
        if nums[i] > 0:
            if pos != -1:
                if nums[i] > nums[pos]: inc_length[i] = pos - i
                else: inc_length[i] = inc_length[i + 1] + 1
            pos = i
        elif i != n - 1:
            inc_length[i] = inc_length[i + 1] + 1
    
    dec_length = [1] * n
    pos = -1
    
    for i in range(n):
        if nums[i] > 0:
            if pos != -1:
                if nums[i] > nums[pos]: dec_length[i] = i - pos
                else: dec_length[i] = dec_length[i - 1] + 1
            pos = i
        elif i > 0:
            dec_length[i] = dec_length[i - 1] + 1
    
    for i in range(3, n + 1):
        flg = True
        for j in range(0, n, i):
            l = j
            r = fmin(j + i - 1, n - 1)
            if inc_length[l] + dec_length[r] < r - l + 2 or r - l + 1 < 3 or inc_length[l] < 2 or dec_length[r] < 2:
                flg = False
        if flg:
            print('Y')
            break
    else:
        print('N')
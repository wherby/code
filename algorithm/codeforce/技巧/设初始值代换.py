# https://codeforces.com/gym/104114/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0706/solution/cf104114g.md
# 带入初始值，把所有表示变成其次式分类
# 如果假设第一项为x,则所有奇数项经过计算都会成为 x +bi 的形式，偶数项变成 -x+bi 的形式， 
# 所以把奇偶分别记录，然后取各自最小值，把r的最小值带入计算。
# 对于奇数项的时候， r_min = x  + min(bi)  => x = r_min- min(bi)
# 对于偶数项 ：    r_min = -x + min(bi)  => x= min(bi) -r_min

import init_setting
from cflibs import *
def main():
    n = II()
    xs = LII()
    rs = LII()
    
    v_pos = [0]
    v_neg = []
    
    for i in range(1, n):
        if i % 2: v_neg.append(xs[i] - xs[i - 1] - v_pos[-1])
        else: v_pos.append(xs[i] - xs[i - 1] - v_neg[-1])
    
    rs.sort()
    min_r = rs[0]
    print(v_pos,v_neg)
    def check(x):
        tmp = [x]
        for i in range(1, n):
            tmp.append(xs[i] - xs[i - 1] - tmp[-1])
        
        if sorted(tmp) == rs:
            exit(print(' '.join(map(str, tmp))))
    
    v_mi = min(v_pos)
    check(min_r - v_mi)
    
    v_mi = min(v_neg)
    check(v_mi - min_r)

main()

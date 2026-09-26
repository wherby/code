# https://codeforces.com/gym/104017/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0820/solution/cf104017b.md
# 枚举矩形4个点的排列，其中3个点能构成顺序连接，利用中点枚举所有可能的顺序3连
# A<B<C 这时D是B的对角点， D不同取值可能构成 （A,B)(C,D), (A,D)(B,C) 这都是可选状态
# 而正常的状态 的时候，中间点有2个不同的选择都会被选中，所以需要除2 


import init_setting
from cflibs import *
def main():
    n = II()
    
    pos = [0] * (n * n + 1)
    
    for i in range(n):
        nums = LII()
        for j in range(n):
            pos[nums[j]] = (i, j)
    
    ans = 0
    
    c_row = [0] * n
    c_col = [0] * n
    
    for i in range(1, n * n + 1):
        x, y = pos[i]
        
        ans += c_row[x] * (n - 1 - c_col[y])
        ans += c_col[y] * (n - 1 - c_row[x])
        
        c_row[x] += 1
        c_col[y] += 1
    
    print(ans // 2)
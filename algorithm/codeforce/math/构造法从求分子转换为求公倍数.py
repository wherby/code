# https://codeforces.com/gym/106247/problem/2
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0220/solution/cf106247b.md
# 构造法，从一个数求因子相等，转换为因子的公倍数问题，构造公倍数等于因子的问题，最后构造出一个满足条件的数列即可
# （1/2+1/3 + 1/6) =1 1/2 + 1/4 + 1/8 + 1/16 + ... + = 1-1/(2^(n-3))
#  最后一项用 三项凑成一个数列
#  1/2 + 1/4 + 1/8 + 1/16 + ... + 1/(2^(n-3)) = 1 - 1/(2^(n-3)) = 1- (1/2+1/3+1/6)/(2^(n-3)) 
# 左右两边乘 3*2^(n-2) 就得到 3*2^(n-3)+3*2^(n-4)+...+3*2 = 3*2^(n-2) - (3+2+1)




import init_setting
from cflibs import *
def main(): 
    n = II()
    if n == 1:
        print(1)
        print(1)
    elif n == 2:
        print(-1)
    else:
        print(3 << n - 2)
        print(1, 2, *(3 << i for i in range(n - 2)))

# https://codeforces.com/gym/105790/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1222/solution/cf105790k.md
# 把乘法变成取模变加法 指数运算的时候用mod -1 取模
# 斐波那契 的矩阵表示


import init_setting
from cflibs import *
from lib.max_pow import *
def main():  
    n = II()
    mod = 998244353
    print(pow(2, matrix_pow([[1, 1], [1, 0]], n, mod - 1)[0][1], 998244353))

main()
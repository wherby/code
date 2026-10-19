# https://codeforces.com/gym/102365/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1012/solution/cf102365c.md
# 贪心寻找边界。



import init_setting
from cflibs import *
def main():
    n = II()
    leaf = 2
    
    for i in range(3, n + 1):
        print('?', 1, leaf, i, flush=True)
        if II(): leaf = i
    
    print('!', leaf)
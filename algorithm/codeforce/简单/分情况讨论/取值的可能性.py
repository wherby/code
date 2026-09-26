# https://codeforces.com/gym/106642/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0813/solution/cf106642e.md
# 这里所有的值的E(rs)/n = 1 ,且必须有2和0，且2和0是成对出现的，因为均值为1， 并且两者不能相邻


import init_setting
from lib.cflibs import *
def main():
    n = II()
    rs = LII()

    if 0 not in rs or 2 not in rs: print('NO')
    else:
        rs = [r for r in rs if r != 1]
        print('NO' if len(rs) % 2 or any(rs[i - 1] == rs[i] for i in range(1, len(rs))) else 'YES')
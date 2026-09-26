# https://codeforces.com/gym/106642/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0813/solution/cf106642d.md
# 因为已知sum(ci)=a ,所以 ci <=a ,且 G(a+1)=b ,所以 ci对应于 多项式的最小系数表示
# 因为ci>=0, 如果某一位不是最小表示，则其他的剩余值的ci > a  或者  <0


import init_setting
from cflibs import *
def main():
    a, b = MII()
    a += 1
    
    ans = []
    while b:
        ans.append(b % a)
        b //= a
    
    print(len(ans))
    print(' '.join(map(str, ans)))
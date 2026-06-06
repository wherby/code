# https://codeforces.com/gym/105010/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0530/solution/cf105010d.md
# 出去开始就输的情况，至少有2个不能整除
# 如果有3不同，则这3个不通过的一定是最后消耗，因为先手使得3个不整除的最多变成2个不整除，必然失败。所以这时就要消耗整除数字，就和n奇偶性有关了
# 如果大于3个不同，大于的部分和整除的数字一样，一旦变成3个不同就是胜负手， 然而这种情况也和n的奇偶性有关



import init_setting
from cflibs import *
def main():
    n, k = MII()
    nums = LII()
    
    c = 0
    for x in nums:
        if x % k: c += 1
    
    if c == 0:
        print('Rami')
    elif c == 2:
        print('Oussama')
    else:
        print('Oussama' if n % 2 == 0 else 'Rami')
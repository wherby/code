# https://codeforces.com/gym/104772/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0918/solution/cf104772d.md
# 因为为了更好构造数字，所以选择10为底， 而费马小定理需要d与10互质。所以需要去掉原始数字的2和5的成分
#  /Users/tao/software/code/algorithm/codeforce/数论/test/测试欧拉定理.py 如果用欧拉定理构造数字，有可能会得到很长的位数，
# 不如直接遍历寻找，只需要d次循环一定能找到
# 𝑑<1000 则最多有12个2，所以后面加13个0



import init_setting
from cflibs import *
def main():
    d = II()
    saved = d
    
    while d % 2 == 0:
        d //= 2
    
    while d % 5 == 0:
        d //= 5
    
    cur = 0
    tot = 0
    
    for i in range(1, 10 ** 6):
        cur = (cur * 10 + 9) % d
        tot = (tot + 9) % saved
        
        if cur == 0 and tot == 0:
            print('9' * i + '0' * 13)
            break
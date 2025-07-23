# https://codeforces.com/problemset/problem/103/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0721/solution/cf103c.md
# 计算设计概率分布，如果是偶数的时候，可以设计1/2的分布。如果是奇数，假设（2,5） -》 （1,4），（1,1） 的分布 期望为 4*(1/2) + 0  （1,2),(1,3) 的分布为 2*（1/2) + 3*(1/3) 这时的期望相等，但是第一个分布的字典序更小
# 所以根据k,和N的关系，压缩密度高的在后面来提高字典序，如果K小，则后K个偶数位为X，如果K 大，则 所有偶数位，和最后的奇数位为X

import init_setting
from cflibs import *
def main():
    n, k, p = MII()
    outs = []

    for _ in range(p):
        x = II()
        
        if k == 0: outs.append('.')
        else:
            vn, vk = n, k
            if n % 2:
                if x == n:
                    outs.append('X')
                    continue
                else:
                    vn -= 1
                    vk -= 1
            
            if vk * 2 <= vn:
                if x % 2 == 0 and x // 2 + vk > vn // 2:
                    outs.append('X')
                else:
                    outs.append('.')
            else:
                if x % 2 == 0: outs.append('X')
                elif (x + 1) // 2 + (vk - vn // 2) > vn // 2:
                    outs.append('X')
                else: outs.append('.')

    print(''.join(outs))
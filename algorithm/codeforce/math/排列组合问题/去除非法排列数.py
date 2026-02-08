# https://codeforces.com/gym/105198/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0129/solution/cf105198k.md
# 求排列数量满足 存在至少一个男孩左边有超过x个女孩，且存在至少一个男孩右边有超过y个女孩
# 等价于 求排列数量 减去 不存在男孩左边有超过x个女孩 和 不存在男孩右边有超过y个女孩
# 用反射原理计算 不存在男孩左边有超过x个女孩 的排列数量
# 不符合的情况就是第x个女孩。和右数第y个女孩之间没有男孩，就是把这些女孩当成一个整体，然后女孩就只有x+y -1 个“独立个体”， 加上男孩数量b，一共b + x + y -1 个个体排列


import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main(): 
    t = II()
    outs = []
    
    M = 2 * 10 ** 6
    mod = 10 ** 9 + 7
    f = Factorial(M, mod)
    
    for _ in range(t):
        b, g, x, y = MII()
        if x + y > g: outs.append(0)
        else: outs.append((f.combi(b + g, b) - f.combi(b + x + y - 1, b)) % mod)
    
    print('\n'.join(map(str, outs)))
# https://codeforces.com/gym/106619/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0716/solution/cf106619d.md
# 选择构造寻路法，
# 这里通过对每一位测试，可以得到 x xor y 的 异或值
# 这里对于所有的位，就可以知道，有异或为1，或者异或为0 的两种情况， 所以就有了 2**n 种可能？
# 但是因为已知异或为 1 的位数，从中选任何一个位置(最低位)， 开始做寻路试探查找。则以此位作为起点，此位一定是某数的子集，然后探索未知位置，如果未知位置置位 满足结果是1，则此数的置位为1，否则为0
# 其实是在一个2分图上试探求解的过程？


import init_setting
from lib.cflibs import *
def main():
    def query(m, v):
        print('?', m, v, flush=True)
        return II()
    
    def answer(x, y):
        print('!', x, y, flush=True)
    
    t = II()
    outs = []
    
    for _ in range(t):
        xor_val = 0
        
        for i in range(60):
            if query(1 << i, 1 << i):
                xor_val |= 1 << i
    
        v = xor_val & -xor_val
        
        for i in range(60):
            if v >> i & 1: continue
            nv = v | (1 << i)
            if query(nv, nv):
                v = nv
        
        x = v
        y = x ^ xor_val
        
        if x > y: x, y = y, x
        
        answer(x, y)
# https://codeforces.com/gym/104017/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0820/solution/cf104017e.md
# 按照题意，可以知道 AB和BA, BC和CB 是等价的
# 意味急着 B是在这个字符串里可以随便移动，所以把B都移动到字符串前段，则后段一定是A，C组合，而相邻等项是可以消除的，所以就是看最后留下的B的奇偶性是否一致和AC的排列是否一致
# 这些都可以用stack处理


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    def f(x):
        cb = 0
        stk = []
        
        for c in x:
            if c == 'B': cb ^= 1
            elif stk and stk[-1] == c: stk.pop()
            else: stk.append(c)
        
        return cb, stk
    
    for _ in range(t):
        outs.append('YES' if f(I()) == f(I()) else 'NO')
    
    print('\n'.join(outs))
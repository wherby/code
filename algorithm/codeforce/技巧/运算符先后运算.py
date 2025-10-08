# https://codeforces.com/gym/104679/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1008/solution/cf104679f.md
# 题目要求是or 和xor 的运算限制，必然是先算or 得到可能的子数组
# 在运算满足 xor的时候，还需要再次验证or条件是否继续满足



import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        a, b = MII()
        
        if a | b != a: outs.append('-1')
        else:
            vals = [i for i in range(a + 1) if i & a == i]
            xor_val = reduce(xor, vals) ^ b
            
            if xor_val: vals.remove(xor_val)
            
            if reduce(ior, vals) == a:
                outs.append(str(len(vals)))
                outs.append(' '.join(map(str, vals)))
            else:
                outs.append('-1')
    
    print('\n'.join(outs))
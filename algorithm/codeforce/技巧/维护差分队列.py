# https://codeforces.com/problemset/problem/283/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0815/solution/cf283a.md
# 用adds数组维护了一个差分队列，这里前n项，所以只用记录增加量就可以了

import init_setting
from cflibs import *
def main():
    n = II()
    
    vals = [0]
    adds = [0]
    outs = []
    
    total = 0
    
    for _ in range(n):
        op = LII()
        if op[0] == 1:
            cnt = op[1]
            val = op[2]
            
            total += cnt * val
            adds[cnt - 1] += val
        
        elif op[0] == 2:
            val = op[1]
            total += val
            
            vals.append(val)
            adds.append(0)
        
        else:
            adds[-2] += adds[-1]
            total -= adds[-1] + vals[-1]
            
            vals.pop()
            adds.pop()
        
        outs.append(total / len(vals))
    
    print('\n'.join(map(str, outs)))
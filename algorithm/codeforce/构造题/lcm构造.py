# https://codeforces.com/gym/106631/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0731/solution/cf106631a.md
# d := lcm(a,b), d = a*b / gcd(a,b)
# e := lcm(a*d,b) = a*d 因为 d%b ==0
# 


import init_setting
from cflibs import *
def main():
    t = II()
    
    for _ in range(t):
        print('MUL', 1, flush=True)
        lcm_val = II()
        print('MUL', lcm_val, flush=True)
        lcm_val_a = II()
        a = lcm_val_a // lcm_val
        print('DIV', lcm_val_a, flush=True)
        b = II()
        print('ANS', a, b, flush=True)
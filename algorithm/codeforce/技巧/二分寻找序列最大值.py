# https://codeforces.com/gym/104020/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0207/solution/cf104020j.md
# 二分可能的最大值，每次进入循环都会增大最大值

import init_setting
from cflibs import *
from math import random

def main(): 
    def query(x, y):
        print('?', x, y, flush=True)
        return I()[0] == 'b'
    
    w, h = MII()
    
    to_check = list(range(1, w + 1))
    random.shuffle(to_check)
    
    idx = 1
    cur_h = 0
    
    for i in to_check:
        if cur_h < h and query(i, cur_h + 1):
            l, r = cur_h + 1, h
            
            while l <= r:
                mid = (l + r) // 2
                if query(i, mid): l = mid + 1
                else: r = mid - 1
            
            idx = i
            cur_h = r
    
    print('!', idx, cur_h)
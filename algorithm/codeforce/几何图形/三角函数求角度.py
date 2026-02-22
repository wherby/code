# https://codeforces.com/gym/106369/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0218/solution/cf106369d.md



import init_setting
from lib.cflibs import *

def main(): 
    y, x, r = MII()
    x = abs(x)
    
    if x * x * y * y > r * r * (x * x + y * y):
        print(-1)
    elif r >= x:
        print(0)
    else:
        print((math.asin(y / math.hypot(x, y) / r * x) - math.atan2(y, x)) / math.pi * 180)
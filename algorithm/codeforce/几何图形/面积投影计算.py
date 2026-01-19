# https://codeforces.com/gym/104149/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0116/solution/cf104149i.md
# 如果布料不够的时候，就需要伞不能撑开，这时先求弧度，然后求投影长度


import init_setting
from lib.cflibs import *
def main(): 
    a, b = map(float, input().split())
    
    v = 4 * b * b * math.sin(math.pi / 4)
    
    if a >= v: print(v)
    else:
        theta = math.asin(a / 4 / b / b) / 2
        w = b * math.sin(theta)
        print(w * w / math.tan(math.pi / 8) * 8)
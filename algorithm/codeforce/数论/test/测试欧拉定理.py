# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0918/solution/cf104772d.md
import random
import init_setting
from cflibs import *
from lib.欧拉数 import getPhi
import math




if __name__ == '__main__':
    x = random.randint(2,1000)
    while x %2==0:
        x = x //2
    while x %5==0:
        x = x//5
    phi = getPhi(10001)
    idt = math.lcm(x,phi[x])
    print(x,(10**idt -1)%x)
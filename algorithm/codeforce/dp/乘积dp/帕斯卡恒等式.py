# C(x+1,n+1)=C(x,n+1)+C(x,n)
# C(x,x)+ C(x,x+1) + C(x,x+2) + C(x,n) == C(x+1,n+1)
import sys,os
parent_directory_concise = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_directory_concise)

import init_setting

from lib.combineWithPreCompute import Factorial

f = Factorial(10000)

def getMid(mid):
    acc =0 
    for a in range(mid,10000):
        acc += f.comb(a,mid)
    return acc

mid = 4
print(getMid(mid)%f.MOD)
print(f.comb(10000,mid+1))

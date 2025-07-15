# 
from functools import cache


n = 13

@cache
def getstate(state:int,used):
    if used == 0:
        return 1 
    idx = state.bit_count()
    ret = 0
    for i in range(n):
        if used &(1<<i):
            t = (idx + 1+i)%n +1
            if (1<<t)& state == 0:
                ret += getstate(state + (1<<t),used - (1<<i))
    return ret

print(getstate(0, (1<<n) -1))

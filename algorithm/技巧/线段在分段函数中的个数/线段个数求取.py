# 求[l,r]线段在分段函数（f(x) =int(log(x)）的个数
#  [求解值在分段函数的个数的2阶技巧](../codeforce/技巧/求在分段函数中的个数.py)
def getNBase(l,r, nbase = 2):
    xl,xr = 1,nbase
    ret = {}
    for i in range(0,64):
        vl = max(l,xl)
        vr = min(r,xr)

        if vl >=vr:continue 
        ret[i] = vr-vl 
        xl,xr = xl*nbase,xr*nbase 
    return ret 

re = getNBase(1,100)
print(re)
re = getNBase(1,100,3)
print(re)
from collections import defaultdict,deque
from math import log
cnt = defaultdict(int)
for i in range(1,100):
    cnt[int(log(i,3))] +=1
print(cnt)

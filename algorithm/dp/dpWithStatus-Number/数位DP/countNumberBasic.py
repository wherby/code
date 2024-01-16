from functools import cache

high = 1123456
high = str(high)
n = len(high)

@cache 
def dfs(i:int, limit_hight):
    if i == n:
        return 1 
    lo =0
    hi = int(high[i]) if limit_hight else 9
    
    res =0 
    for d in range(lo,hi+1):
        res += dfs(i+1,limit_hight and d ==hi)
    return res 

print(dfs(0,True)) 
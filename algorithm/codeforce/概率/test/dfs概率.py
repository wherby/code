# https://codeforces.com/gym/106160/problem/A
from functools import cache
s = "31415926535897932384626433832795028841971693993751"
s  ="12345"
n = len(s)
ans = 0
delta =10**(-20)

@cache
def dfs(idx,acc ,sig):
    
    if idx ==n:
        return  acc*sig
    ret =0
    
    cur = acc*10+int(s[idx])
    ret +=  dfs(idx+1,cur,sig) *0.1
    ret += dfs(idx+1, 0,-1)*0.45
    ret += sig * cur*0.9
    ret += dfs(idx+1,0, 1)*0.45
    return ret 

print(dfs(0,0,1))


# combination 和式

f[k](n) =C(n,0)+C(n,1) + ...+C(n,k)
f[k](n+1) = C(n+1,0) + C(n+1,1) +...C(n+1,k)

其中
f[k](n+1) = f[k](n) *2 - C(n,k)
意义就是在(n+1)个数字中取得[0,k]个数字，对于第n+1个数字加入，等于前N个数字取[0,k]个和前N个数字取[0,k-1]个数字，所以可以*2减去C(n,k)

因为 C(n,k) = C(n-1,k) + C(n-1,k-1)
f[k](n+1) = C(n+1,0) + C(n+1,1) +...C(n+1,k)
          =[C(n,0),C(n,-1)] + [C(n,0),C(n,1)] +...+[C(n,k-1),C(n,k)]
          = 2*[C(n,0)+ C(n,1)+...+C(n,k-1)] + C(n,k)
          =2*f[k](n) -C(n,k)

https://leetcode.cn/circle/discuss/DW1adK/ 

![pic](Screenshot%202025-01-19%20at%2019.48.44.png)

# 奇偶项和相等
algorithm/mathA/combination特性/鸡偶项和.py

```python
cmb = Factorial(10000)
@cache
def getI(mx):
    ret = 0
    for i in range(1,mx+1,2):
        ret += cmb.comb(mx,i)
        ret = ret%MOD 
    return ret

for i in range(1,10000):
    if getI(i)!=pow(2,i-1,MOD):
        print(getI(i),  pow(2,i-1,MOD))
```

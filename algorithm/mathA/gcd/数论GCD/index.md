

## 数轴抽象
假设自然数是 1,2,3,4..N的数轴 N
则 K,2K,3K,...NK 的数字缩放 也可以变成 1,2,3..N 的数轴 N‘

在数轴N上的关系也在虚拟缩放数轴上可以重复

## 一个数组中GCD为K的子数组长度为M有多少
[直接求解GCD数字](另一解法sorted-gcd-pair-queries.py)
利用莫比乌斯特性，先求出可以被数组中元素k的计数c， 就能用容斥原理，获取任一值gcd为k的 m个长度子数组的数量
```python
def getMlengthGcd(ls,m,queries):
    c = Counter(ls)
    mx = max(ls)
    mu, F, primes = prepare(mx+1)
    gcd_count = [0]*(mx+1)
    for i in range(1,mx+1):
        for j in range(i*2,mx+1,i):
            c[i] += c[j]
    #print(c)
    for i in queries:
        gcd_count[i] += math.comb(c[i],m)
        for j in range(2,mx//i +1):
            gcd_count[i] += mu[j]*math.comb(c[j*i],m)
    return gcd_count
```

## 倍数容斥
https://leetcode.cn/problems/count-ways-to-choose-coprime-integers-from-rows/solutions/3815551/liang-chong-fang-fa-dong-tai-gui-hua-bei-4djl/

[倍数容斥](mlengthGcdSubArray倍数容斥.py)

## gcd 容斥和 裴蜀定理 
[gcd倍数容斥和 裴蜀定理 ](../../../../contest/meta2023/r2/q5/qn.py)


## SOS DP 
[SOS DP](../../../dp/SOSDP)


# 问题
有n 个数字，可以在[1,m]中选择，使得n个数字等于target的组合有多少个

如果没有[1,m]的限制，则问题就是target个小球中间放 n-1个隔板， comb(target -1 ,n-1)

由于有数字区间的限制，则可以用二进制反演，枚举有多少个数字可能会大于m，使用容斥原理

```python
for i in range(target // (m + 1) + 1):
    total = target - i * m
    ans += f.combi(total - 1, n - 1) * f.combi(n, i) % mod * (1 if i % 2 == 0 else -1) % mod
    ans %= mod
```

遍历可能有几个数字超过m,然后减去m 再["加上"[(二进制反演)后的数字在原图上的途径

# 把n个种类的小球分配到k个盒子的分法
https://codeforces.com/gym/103821/problem/J
https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0708/solution/cf103821j.md
错误路线：
ai个不同种类的小球，分配到恰好k个盒子的分法 f(i)： 
g(i) 表示把小球分配到不超过i个盒子的分法
则 f(1) = g(1)-g(0)=g(1)
f(2) = g(2) - g(1)
f(3) = g(3)-g(2)   
[上面这样思考是错误的](二项式反演容易错误.md)

因为对于k个选择盒子而言，g(i) 的时候需要考虑先在k个盒子选择i个，所以递推的时候系数就不是齐次的了，系数变成二项式，
所以需要使用二项式反演的方法确定递推式：正是因为 $\binom{i}{j}$ 导致了不同层级之间的方案重叠是“加权”的，所以我们需要交替的 $(-1)^{i-j}$ 和同样的二项式系数去精细地把那些“多算的权重”给扣掉。
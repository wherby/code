

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
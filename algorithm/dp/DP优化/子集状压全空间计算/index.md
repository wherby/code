
# 
https://leetcode.cn/problems/minimum-cost-to-merge-sorted-lists/

## 计算全空间DP

```python
for i,a in enumerate(lists):
    high_bit = 1<<i 
    for s in range(high_bit):
        t = high_bit | s 
        sum_len[t] = sum_len[s] + len(a)
        b = sorted[s] + a 
        b.sort()
        sorted[t] = b 
        median[t] = b[(len(b) -1)//2]
```

## 计算每个状态的子集 

```python
for i in range(N):
    if i & (i-1) ==0:
        dp[i] = 0 
        continue
    # 枚举 i 的非空真子集 j
    j = i&(i-1)
    while j > (i^j):  ## 因为划分为左右两个对等的部分，所以只计算其中 a>b 部分的值
        k = i^j
        dp[i] = min(dp[i], dp[j] + dp[k] + sum_len[i]+ abs(median[j] - median[k]) )
        j = (j-1)&i
```
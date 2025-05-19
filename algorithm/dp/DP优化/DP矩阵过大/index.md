

# 如果N不大的时候 DP矩阵建立
https://codeforces.com/problemset/problem/1970/E2
http://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0514/solution/cf1970e2.md

```python
def main():
    n, k = MII()
    ss = LII()
    ls = LII()

    for i in range(n):
        ss[i] += ls[i]

    grid = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            grid[i][j] = ss[i] * ss[j] - ls[i] * ls[j]

    res = matrix_pow(grid, k)

    print(sum(res[0]) % mod)
```

# 如果N过大的时候，需要压缩状态
https://codeforces.com/problemset/problem/1970/E3
https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0517/solution/cf1970e3.md

```python
def main():
    n, k = MII()

    ss = LII()
    ls = LII()

    grid = [[0, 0], [0, 0]]

    for i in range(n):
        grid[0][0] = (grid[0][0] + (ls[i] + ss[i]) * ss[i]) % mod
        grid[0][1] = (grid[0][1] + (ls[i] + ss[i]) * ls[i]) % mod
        grid[1][0] = (grid[1][0] + ss[i] * ss[i]) % mod
        grid[1][1] = (grid[1][1] + ss[i] * ls[i]) % mod

    total_s = sum(ss) % mod
    total_l = sum(ls) % mod

    res = matrix_pow(grid, k - 1)

    ans = 0
    ans += (ss[0] * res[0][0] + ls[0] * res[1][0]) * (total_s + total_l)
    ans += (ss[0] * res[0][1] + ls[0] * res[1][1]) * total_s

    print(ans % mod)
```
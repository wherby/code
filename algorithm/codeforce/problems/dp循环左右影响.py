# https://codeforces.com/problemset/problem/212/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0411/solution/cf212c.md
# AB =>BA  AA =>AA BA =>BA BB =>BB
# 当前为A(往右)，则上一个值的上一个状态是A或者B, 如果 ？？
# 先假设一个状态，循环一周回到这个状态的倍数？

from cflibs import *

def main():
    s = I()
    n = len(s)

    s += s[0]

    ans = 0

    # A 作为开头
    dp0, dp1 = 1, 0

    for i in range(n):
        if s[i] == 'A':
            dp0, dp1 = dp0 + dp1, (0 if s[i + 1] == 'A' else dp1)
        else:
            dp0, dp1 = dp1, (dp0 if s[i + 1] == 'A' else dp1)

    ans += dp0

    # B 作为开头
    dp0, dp1 = 0, 1

    for i in range(n):
        if s[i] == 'A':
            dp0, dp1 = dp0 + dp1, (0 if s[i + 1] == 'A' else dp1)
        else:
            dp0, dp1 = dp1, (dp0 if s[i + 1] == 'A' else dp1)

    ans += dp1

    print(ans)


#     解法思路（基于提示）
# 关键观察
# 环形问题转化为链式问题：

# 由于牛仔是围成一圈的，直接处理环形结构比较复杂。

# 提示建议将环形问题转化为链式问题：假设有一个长度为 n+1 的链，其中第 n+1 个牛仔的状态必须与第 1 个牛仔相同（以保证环形闭合）。

# 动态规划（DP）：

# 定义 dpA[i] 和 dpB[i]：

# dpA[i]：前 i 个牛仔已经处理，且第 i 个牛仔在调整前是 'A' 的方案数。

# dpB[i]：前 i 个牛仔已经处理，且第 i 个牛仔在调整前是 'B' 的方案数。

# 我们需要通过 DP 递推关系计算 dpA[i+1] 和 dpB[i+1]。

# DP 递推关系：

# 对于第 i+1 个牛仔，我们需要确保第 i 个牛仔的状态在调整后与 s[i] 一致。

# 具体分为以下情况：

# 如果 s[i] = 'A'：

# 如果第 i+1 个牛仔调整前是 'A'，则第 i 个牛仔可以是 'A' 或 'B'（因为 'A' 和 'A' 不会翻转）。

# 如果第 i+1 个牛仔调整前是 'B'，则第 i 个牛仔必须是 'B'（因为 'BA' 会翻转成 'AB'，即 s[i] = 'A'）。

# 如果 s[i] = 'B'：

# 如果第 i+1 个牛仔调整前是 'A'，则第 i 个牛仔必须是 'A'（因为 'AB' 会翻转成 'BA'，即 s[i] = 'B'）。

# 如果第 i+1 个牛仔调整前是 'B'，则第 i 个牛仔可以是 'A' 或 'B'（因为 'B' 和 'B' 不会翻转）。

# 初始化：

# 由于是环形问题，我们需要枚举第 1 个牛仔的状态（'A' 或 'B'）：

# 如果第 1 个牛仔是 'A'，则 dpA[1] = 1，dpB[1] = 0。

# 如果第 1 个牛仔是 'B'，则 dpA[1] = 0，dpB[1] = 1。

# 环形闭合条件：

# 最终，第 n+1 个牛仔的状态必须与第 1 个牛仔的状态相同。

# 因此，我们需要分别计算：

# 第 1 个牛仔是 'A' 时，第 n+1 个牛仔是 'A' 的方案数。

# 第 1 个牛仔是 'B' 时，第 n+1 个牛仔是 'B' 的方案数。

# 将两者相加即为答案
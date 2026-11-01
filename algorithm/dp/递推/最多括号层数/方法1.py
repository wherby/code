# https://codeforces.com/gym/105477/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1023/solution/cf105477b.md
# 求最深层数为H的L对括号匹配

import sys


def main():
  mod = 1000000007
  max_H = 200
  max_len = 400

  # saved[h][l] 存储：半长度为 l、最大高度恰好为 h 的方案数
  saved = [[0] * (max_len // 2 + 1) for _ in range(max_H + 1)]

  # dp[x][y] 表示：历史最大高度为 x，当前高度为 y 的方案数
  # 初始化：起点时最大高度为 0，当前高度为 0
  dp = [[0] * (max_H + 1) for _ in range(max_H + 1)]
  dp[0][0] = 1

  # 逐步迭代总长度 (最多 400 步，对应半长度 200)
  for i in range(1, max_len + 1):
    ndp = [[0] * (max_H + 1) for _ in range(max_H + 1)]

    for x in range(max_H + 1):
      for y in range(x + 1):  # 当前高度 y 不可能超过最大高度 x
        if not dp[x][y]:
          continue
        val = dp[x][y]

        # 1. 向下走 (y -> y - 1)，前提是 y >= 1
        if y >= 1:
          ndp[x][y - 1] = (ndp[x][y - 1] + val) % mod

        # 2. 向上走 (y -> y + 1)，新高度为 y + 1，最大高度更新为 max(x, y + 1)
        nx = max(x, y + 1)
        if nx <= max_H:
          ndp[nx][y + 1] = (ndp[nx][y + 1] + val) % mod

    dp = ndp

    # 当总步数 i 为偶数时，对应合法的半长度 l = i // 2
    if i % 2 == 0:
      l = i // 2
      for h in range(max_H + 1):
        # 此时 dp[h][0] 正好代表：最大高度恰好为 h 且最终回到地面的方案数
        saved[h][l] = dp[h][0]

  # 快速读取输入并输出查询结果
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  t = int(input_data[0])
  idx = 1
  outs = []

  for _ in range(t):
    l = int(input_data[idx])
    h = int(input_data[idx + 1])
    idx += 2
    outs.append(str(saved[h][l]))

  print("\n".join(outs))


if __name__ == "__main__":
  main()
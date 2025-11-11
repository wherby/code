
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/C?source=facebook

import sys

INF = 10**18

def solve():
    R, C = map(int, sys.stdin.readline().split())
    print(f"R: {R}, C: {C}", file=sys.stderr)
    
    A = []
    for i in range(R):
        row = list(map(int, sys.stdin.readline().split()))
        A.append(row)
    
    # f[i][j]: 从 (0,0) 到 (i,j) 的最大路径和
    f = [[0] * C for _ in range(R)]
    # g[i][j]: 从 (i,j) 到 (R-1,C-1) 的最大路径和
    g = [[0] * C for _ in range(R)]
    
    # 计算 f (左上到右下)
    for i in range(R):
        for j in range(C):
            if i > 0:
                f[i][j] = max(f[i][j], f[i-1][j])
            if j > 0:
                f[i][j] = max(f[i][j], f[i][j-1])
            f[i][j] += A[i][j]
    
    # 计算 g (右下到左上)
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if i < R-1:
                g[i][j] = max(g[i][j], g[i+1][j])
            if j < C-1:
                g[i][j] = max(g[i][j], g[i][j+1])
            g[i][j] += A[i][j]
    
    # 初始化三维DP数组
    # dp1[i][j][x]: Plankton在(i,j)，垂直方向，线段起始行x
    dp1 = [[[INF] * R for _ in range(C)] for _ in range(R)]
    # dp2[i][j][y]: Plankton在(i,j)，水平方向，线段起始列y  
    dp2 = [[[INF] * C for _ in range(C)] for _ in range(R)]
    
    # 初始化：Plankton起点在(0, C-1)
    dp1[0][C-1][0] = 0
    dp2[0][C-1][C-1] = 0
    
    # DP转移
    for i in range(R):
        for j in range(C-1, -1, -1):
            # 从dp1转移（垂直方向）
            for x in range(i + 1):  # x <= i
                if dp1[i][j][x] >= INF:
                    continue
                    
                # 继续向下（保持垂直方向）
                if i < R - 1:
                    val = dp1[i][j][x]
                    # Krabs可能绕过当前列
                    left_sum = f[i][j-1] if j > 0 else 0
                    right_sum = g[i][j+1] if j < C - 1 else 0
                    new_val = max(val, left_sum + right_sum)
                    if new_val < dp1[i+1][j][x]:
                        dp1[i+1][j][x] = new_val
                
                # 转向左（垂直→水平）
                if j > 0:
                    val = dp1[i][j][x]
                    # Krabs可能从不同路径绕过
                    down_sum = g[i+1][j] if i < R - 1 else 0
                    path1 = f[x-1][j] if x > 0 else 0
                    path2 = f[i-1][j-1] if i > 0 else 0
                    new_val = max(val, down_sum + max(path1, path2))
                    if new_val < dp2[i][j-1][j]:
                        dp2[i][j-1][j] = new_val
            
            # 从dp2转移（水平方向）
            for y in range(j, C):  # y >= j
                if dp2[i][j][y] >= INF:
                    continue
                    
                # 转向下（水平→垂直）
                if i < R - 1:
                    val = dp2[i][j][y]
                    left_sum = f[i][j-1] if j > 0 else 0
                    path1 = g[i][y+1] if y < C - 1 else 0
                    path2 = g[i+1][j+1] if j < C - 1 else 0
                    new_val = max(val, left_sum + max(path1, path2))
                    if new_val < dp1[i+1][j][i]:
                        dp1[i+1][j][i] = new_val
                
                # 继续向左（保持水平方向）
                if j > 0:
                    val = dp2[i][j][y]
                    down_sum = g[i+1][j] if i < R - 1 else 0
                    up_sum = f[i-1][j] if i > 0 else 0
                    new_val = max(val, down_sum + up_sum)
                    if new_val < dp2[i][j-1][y]:
                        dp2[i][j-1][y] = new_val
    
    # 在终点 (R-1, 0) 找答案
    ans = INF
    for x in range(R):
        ans = min(ans, dp1[R-1][0][x])
    for y in range(C):
        ans = min(ans, dp2[R-1][0][y])
    
    return ans

def main():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    idx = 1
    
    for i in range(1, t + 1):
        print(f"Case #{i}: ", end="")
        result = solve()
        print(result)

if __name__ == "__main__":
    main()
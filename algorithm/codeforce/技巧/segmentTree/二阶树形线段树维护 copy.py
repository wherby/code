# https://codeforces.com/gym/106728/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1001/solution/cf106728c.md
# 用数组模拟，dp 记录最小值， best_child 记录最小值的偏移量，edge_w 记录每个节点出发的路径权值


import sys

# 常见的算法竞赛输入模板函数
def MII():
    return map(int, sys.stdin.readline().split())

def LII():
    return list(map(int, sys.stdin.readline().split()))

def main():
    # 逐行读取输入
    k, l, n = MII()
    ws = LII()

    # 特判 k = 1 的情况（退化为单链）
    if k == 1:
        print(sum(ws) * (l - 1))
        return

    # 1. 计算完全 k 叉树的总节点数 S = (k^l - 1) // (k - 1)
    total_nodes = (k**l - 1) // (k - 1)

    # 2. 初始化状态数组
    # dp[u]: 从节点 u 到其子树叶子的最小白兔数量
    # best_child[u]: 使得权值最小的最左侧子节点索引 (0 到 k-1)
    # edge_w[u][j]: 节点 u 到其第 j 个子节点的当前边权
    dp = [0] * total_nodes
    best_child = [0] * total_nodes
    edge_w = [[0] * k for _ in range(total_nodes)]

    # 3. 逐次模拟 n 次任务
    for w in ws:
        # Step 1: 从根节点 0 出发，根据 best_child 下潜找到最优路径
        path = [0] * l
        curr = 0
        path[0] = curr

        for depth in range(l - 1):
            c = best_child[curr]
            curr = curr * k + 1 + c  # k 进制定位子节点
            path[depth + 1] = curr

        # Step 2: 自底向上回溯，增加边权并更新沿途祖先节点的 dp 和 best_child
        for depth in range(l - 2, -1, -1):
            u = path[depth]
            c = path[depth + 1] - (u * k + 1)  # 还原出选择的是第 c 个子节点
            
            # 增加该段路径的边权
            edge_w[u][c] += w

            # 重新寻找 u 的 k 个子节点中的最左最小值
            min_val = float('inf')
            min_c = 0
            base_child = u * k + 1  # 第 0 个子节点的全局编号

            for j in range(k):
                val = edge_w[u][j] + dp[base_child + j]
                if val < min_val:
                    min_val = val
                    min_c = j

            dp[u] = min_val
            best_child[u] = min_c

    # 第 n+1 次任务的答案即为根节点 0 的 dp 值
    print(dp[0])

if __name__ == '__main__':
    main()
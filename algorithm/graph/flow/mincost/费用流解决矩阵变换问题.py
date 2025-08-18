# https://codeforces.com/problemset/problem/1913/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0816/solution/cf1913e.md
import collections

# 定义边结构
class Edge:
    def __init__(self, to_node, capacity, cost, reverse_edge_idx):
        self.to = to_node            # 边的终点
        self.capacity = capacity     # 边的容量
        self.cost = cost             # 单位流量的费用
        self.rev = reverse_edge_idx  # 反向边在邻接列表中的索引

# 最小费用流图类
class MCFGraph:
    def __init__(self, num_vertices):
        self.V = num_vertices           # 顶点数量 (0 到 V-1)
        self.adj = [[] for _ in range(num_vertices)] # 邻接列表
        
        # 用于 SPFA 算法的辅助数组
        self.dist = [float('inf')] * num_vertices # 距离 (最小费用)
        self.parent_edge = [None] * num_vertices   # 父边在邻接列表中的索引
        self.parent_node = [None] * num_vertices   # 父节点

    def add_edge(self, from_node, to_node, capacity, cost):
        # 添加正向边
        self.adj[from_node].append(Edge(to_node, capacity, cost, len(self.adj[to_node])))
        # 添加反向边 (容量为0, 费用为负, 用于残量图)
        self.adj[to_node].append(Edge(from_node, 0, -cost, len(self.adj[from_node]) - 1))

    def spfa(self, source, sink):
        """
        使用 SPFA 算法寻找从 source 到 sink 的最小费用路径。
        返回 True 如果找到路径，False 否则。
        """
        self.dist = [float('inf')] * self.V
        self.parent_edge = [None] * self.V
        self.parent_node = [None] * self.V
        
        q = collections.deque()
        in_queue = [False] * self.V

        self.dist[source] = 0
        q.append(source)
        in_queue[source] = True

        while q:
            u = q.popleft()
            in_queue[u] = False

            for i, edge in enumerate(self.adj[u]):
                # 如果有剩余容量 且 可以通过这条边找到更短的路径
                if edge.capacity > 0 and self.dist[edge.to] > self.dist[u] + edge.cost:
                    self.dist[edge.to] = self.dist[u] + edge.cost
                    self.parent_node[edge.to] = u
                    self.parent_edge[edge.to] = i # 记录父节点和边的索引
                    if not in_queue[edge.to]:
                        q.append(edge.to)
                        in_queue[edge.to] = True
            
        return self.dist[sink] != float('inf') # 如果终点可达，则找到路径

    def min_cost_flow(self, source, sink, K_max_flow):
        """
        计算从 source 到 sink 的最小费用流。
        s: 源点, t: 汇点, K_max_flow: 期望的总流量。
        返回 (实际推送的总流量, 最小总费用)。
        """
        total_flow = 0
        total_cost = 0

        # 当实际流量小于期望流量 且 还能找到增广路径时循环
        while total_flow < K_max_flow and self.spfa(source, sink):
            # 找到当前路径上可以增广的最大流量 (瓶颈容量)
            path_flow = float('inf')
            curr_node = sink
            while curr_node != source:
                prev_node = self.parent_node[curr_node]
                edge_idx = self.parent_edge[curr_node]
                path_flow = min(path_flow, self.adj[prev_node][edge_idx].capacity)
                curr_node = prev_node
            
            # 限制增广流量不超过K_max_flow的剩余部分
            path_flow = min(path_flow, K_max_flow - total_flow)

            total_flow += path_flow
            total_cost += path_flow * self.dist[sink] # 路径费用 * 流量

            # 沿路径更新边的容量 (正向减, 反向加)
            curr_node = sink
            while curr_node != source:
                prev_node = self.parent_node[curr_node]
                edge_idx = self.parent_edge[curr_node]
                rev_edge_idx = self.adj[prev_node][edge_idx].rev

                self.adj[prev_node][edge_idx].capacity -= path_flow
                self.adj[curr_node][rev_edge_idx].capacity += path_flow
                curr_node = prev_node
            
        return total_flow, total_cost

# --- 主函数用于解决矩阵问题 ---
def solve_matrix_problem(n, m, matrix_a, A_row_sums, B_col_sums):
    # 1. 节点映射:
    # Source: 0
    # Row nodes (R_i): 1 to n (mapping i-th row from A_row_sums to i+1)
    # Col nodes (C_j): n+1 to n+m (mapping j-th col from B_col_sums to n+j+1)
    # Sink: n + m + 1
    
    num_vertices = n + m + 2
    mcf_graph = MCFGraph(num_vertices)

    initial_ones_count = 0 # 统计初始矩阵中 1 的总数

    # 2. 添加边
    # Source to Row nodes
    for i in range(n):
        mcf_graph.add_edge(0, i + 1, A_row_sums[i], 0)

    # Col nodes to Sink
    for j in range(m):
        mcf_graph.add_edge(n + j + 1, n + m + 1, B_col_sums[j], 0)

    # Row nodes to Col nodes (representing matrix cells)
    for i in range(n):
        for j in range(m):
            cost_for_cell = 0
            if matrix_a[i][j] == 0:
                cost_for_cell = 1 # 0->1 变化成本为 1
            else:
                initial_ones_count += 1 # 统计原始 1 的数量
                # 如果 matrix_a[i][j] == 1, 保持 1 不变成本为 0
            
            mcf_graph.add_edge(i + 1, n + j + 1, 1, cost_for_cell) # 容量为1，因为一个单元格只能流过1个1

    # 3. 计算目标总流量 (所有行和 或 所有列和)
    target_flow = sum(A_row_sums)
    
    # 验证总和一致性（一个可行解的必要条件）
    if target_flow != sum(B_col_sums):
        # 理论上，如果问题保证可行，则不会出现这种情况
        # 但在实际中，可能需要处理这种不可能的情况
        print("Error: Sum of row sums does not equal sum of column sums. No solution exists.")
        return -1

    # 4. 运行 Min-Cost Max-Flow
    total_pushed_flow, min_cost_0_to_1 = mcf_graph.min_cost_flow(0, n + m + 1, target_flow)

    # 确保实际推送的流量达到了目标流量（如果未能达到，说明无解或容量限制问题）
    if total_pushed_flow != target_flow:
        print(f"Error: Could not push required flow. Pushed {total_pushed_flow}, required {target_flow}")
        return -1 # 这在完美解的问题中不应该发生，除非容量模型有误

    # 5. 计算最终最小操作数
    # total_operations = (0->1 变化次数) + (1->0 变化次数)
    # min_cost_0_to_1 就是 (0->1 变化次数)
    # (1->0 变化次数) = (初始 1 的总数) - (初始是 1 且最终仍是 1 的单元格数量)
    # 并且 (初始是 1 且最终仍是 1 的单元格数量) = (最终 1 的总数) - (初始是 0 且最终变为 1 的单元格数量)
    # 最终 1 的总数 = target_flow
    # 初始是 0 且最终变为 1 的单元格数量 = min_cost_0_to_1
    
    # 所以，
    # 1->0 变化次数 = initial_ones_count - (target_flow - min_cost_0_to_1)
    
    min_total_operations = min_cost_0_to_1 + \
                           (initial_ones_count - (target_flow - min_cost_0_to_1))
    
    # 简化公式:
    # min_total_operations = 2 * min_cost_0_to_1 + initial_ones_count - target_flow
    
    return min_total_operations

# --- 示例用法 ---
if __name__ == "__main__":
    # 示例 1: 3x3 矩阵
    n1, m1 = 3, 3
    a1 = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]
    A1 = [1, 2, 0]  # 每行的 1 的数量
    B1 = [1, 1, 1]  # 每列的 1 的数量
    
    # 初始 1 的数量: 3
    # 目标 1 的数量: sum(A1) = 1+2+0 = 3
    # sum(B1) = 1+1+1 = 3 (匹配)
    
    # 预期结果分析:
    # 目标:
    # [0,1,0] A=1
    # [1,0,1] A=2
    # [0,0,0] A=0
    # B=[1,1,1]
    
    # 一个可能的最优解 (例如，将 a[2][2] 改为 1):
    # [0,1,0]
    # [1,0,1]
    # [0,0,0] -> a[2][2]=1 (1 operation) -> [0,0,1]
    # Final matrix:
    # [0,1,0] A=1
    # [1,0,1] A=2
    # [0,0,1] A=1 (Oops, A[2] should be 0. This is not a solution.)
    
    # Let's try to transform matrix_a:
    # [0,1,0]  (A=1)
    # [1,0,1]  (A=2)
    # [0,0,0]  (A=0)
    # B=[1,1,1]
    
    # 满足 A 和 B 的一个最终矩阵示例 (可能不是最优操作次数):
    # [0,1,0]   (A=1)
    # [1,0,1]   (A=2)
    # [0,0,0]   (A=0)
    # Sums: [1,2,0], [1,1,1]
    # Initial ones: 3
    # Target ones: 3
    
    # If we convert a[0][1] to 0 (cost 1)
    # And a[0][0] to 1 (cost 1)
    # Original:   [[0,1,0], [1,0,1], [0,0,0]]
    # Intermediate: [[1,0,0], [1,0,1], [0,0,0]] -> 2 ops so far
    # Row sums: [1,2,0] OK
    # Col sums: [2,0,1] -> B is [1,1,1] (Not OK)
    
    # The problem asks for minimum operations.
    # A potential optimal solution (by hand, not guaranteed right):
    # Original:
    # 0 1 0  (A=1)
    # 1 0 1  (A=2)
    # 0 0 0  (A=0)
    # B = [1,1,1]
    
    # Target:
    # 0 1 0  (A=1)  (No change)
    # 1 0 1  (A=2)  (No change)
    # 0 0 0  (A=0)  (No change)
    # Col sums: [1,1,1]
    # All conditions met with 0 operations. This is a possible solution.
    
    # Let's recheck if the initial matrix already matches
    # A1 = [1, 2, 0]  # Row sums desired
    # B1 = [1, 1, 1]  # Col sums desired
    # Initial matrix:
    # Row 0: 0 1 0 (sum=1, matches A[0])
    # Row 1: 1 0 1 (sum=2, matches A[1])
    # Row 2: 0 0 0 (sum=0, matches A[2])
    # Col 0: 0 1 0 (sum=1, matches B[0])
    # Col 1: 1 0 0 (sum=1, matches B[1])
    # Col 2: 0 1 0 (sum=1, matches B[2])
    # Yes, the initial matrix *already* satisfies the conditions! So, 0 operations.

    result1 = solve_matrix_problem(n1, m1, a1, A1, B1)
    print(f"Example 1 Result: {result1}") # Expected: 0

    # 示例 2: 2x2 矩阵，需要更改
    n2, m2 = 2, 2
    a2 = [
        [0, 0],
        [0, 0]
    ]
    A2 = [1, 1]
    B2 = [1, 1]

    # 初始 1 的数量: 0
    # 目标 1 的数量: 2
    # 需要将两个 0 变为 1。最小操作数 2。
    result2 = solve_matrix_problem(n2, m2, a2, A2, B2)
    print(f"Example 2 Result: {result2}") # Expected: 2

    # 示例 3: 2x2 矩阵，1 需要变为 0
    n3, m3 = 2, 2
    a3 = [
        [1, 1],
        [1, 1]
    ]
    A3 = [1, 1]
    B3 = [1, 1]

    # 初始 1 的数量: 4
    # 目标 1 的数量: 2
    # 需要将两个 1 变为 0。最小操作数 2。
    result3 = solve_matrix_problem(n3, m3, a3, A3, B3)
    print(f"Example 3 Result: {result3}") # Expected: 2

    # 示例 4: 2x2 混合
    n4, m4 = 2, 2
    a4 = [
        [1, 0],
        [0, 1]
    ]
    A4 = [1, 1]
    B4 = [1, 1]
    
    # 初始 1 的数量: 2
    # 目标 1 的数量: 2
    # 可能的最终矩阵：
    # [[1,0], [0,1]] (0 ops)
    # [[0,1], [1,0]] (2 ops: 0->1, 1->0)
    # 应该选 0 ops 的那个。
    result4 = solve_matrix_problem(n4, m4, a4, A4, B4)
    print(f"Example 4 Result: {result4}") # Expected: 0



#     最小费用流图（MCFGraph）是一个流网络，其中每条边除了有容量限制外，还有一个单位流量的成本。这种图论模型的目标是：在满足边的容量限制和节点流量平衡的条件下，将一定量的总流量从源点发送到汇点，同时使总的传输成本最小化。

# MCFGraph 的 Python 实现
# 解决你提出的矩阵转换问题，可以将其建模为一个最小费用最大流（Min-Cost Max-Flow）问题。

# 问题建模
# 节点定义:

# S (源点): 编号 0。

# T (汇点): 编号 n + m + 1。

# R_i (行节点): n 个节点，编号从 1 到 n。对应矩阵的每一行。

# C_j (列节点): m 个节点，编号从 n + 1 到 n + m。对应矩阵的每一列。

# 边和费用:
# 我们要将矩阵 a 转换为 a'，使得 a' 的行和列满足给定的 A 和 B 约束。同时，最小化 0->1 和 1->0 的操作次数（每次操作成本为 1）。

# 从 S 到 R_i (源点到行节点):

# 表示第 i 行必须提供 A[i] 个 1。

# 边: S -> R_i (即 0 -> i + 1)

# 容量: A[i]

# 费用: 0 (没有成本)

# 从 C_j 到 T (列节点到汇点):

# 表示第 j 列必须接收 B[j] 个 1。

# 边: C_j -> T (即 n + j + 1 -> n + m + 1)

# 容量: B[j]

# 费用: 0

# 从 R_i 到 C_j (行节点到列节点，代表矩阵单元格 (i, j)):

# 这条边决定了最终矩阵 a'[i][j] 是否为 1。如果流过 1 单位，则 a'[i][j] = 1；否则为 0。

# 边: R_i -> C_j (即 i + 1 -> n + j + 1)

# 容量: 1 (每个单元格只能是 0 或 1)

# 费用:

# 如果初始 a[i][j] == 0: 费用为 1 (表示将 0 变为 1 需要 1 次操作)。

# 如果初始 a[i][j] == 1: 费用为 0 (表示将 1 保持为 1 不需要额外操作)。

# 求解 Min-Cost Max-Flow
# 计算目标总流量: 目标是推动 TARGET_FLOW = sum(A) 单位的流量从 S 到 T。

# 重要: 在一个可行的矩阵中，总行和必须等于总列和，即 sum(A) 必须等于 sum(B)。如果问题没有明确指出，通常会假定输入满足此条件。

# 运行 Min-Cost Max-Flow 算法: 最常用的算法是连续最短路算法（Successive Shortest Path Algorithm）。它通过重复以下步骤直到达到目标流量：

# 在残量图（residual graph，允许流量回退）中，使用SPFA（Shortest Path Faster Algorithm）或带势函数的 Dijkstra 算法找到一条从源点到汇点的最小费用增广路径。

# 沿这条路径增广尽可能多的流量。

# 计算总操作数:

# 让 min_cost_0_to_1 为 MCF 算法得到的最小总费用。这个费用精确地等于所有 0 -> 1 变化的次数。

# 统计初始矩阵中 1 的总数 initial_ones_count。

# 最终矩阵中 1 的总数 final_ones_count 等于 TARGET_FLOW (即 sum(A))。

# 总操作数 = (0->1 的改变次数) + (1->0 的改变次数)

# 1->0 的改变次数可以通过 initial_ones_count 和 min_cost_0_to_1 推导：
# 1->0 改变次数 = initial_ones_count - (初始是 1 且最终仍是 1 的单元格数量)
# 初始是 1 且最终仍是 1 的单元格数量 = final_ones_count - min_cost_0_to_1

# 所以，1->0 改变次数 = initial_ones_count - (final_ones_count - min_cost_0_to_1)

# 最终总操作数 = min_cost_0_to_1 + initial_ones_count - final_ones_count + min_cost_0_to_1

# 最终总操作数 = 2 * min_cost_0_to_1 + initial_ones_count - final_ones_count


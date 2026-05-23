# Not verified, from Gemini


import sys

# 提高 Python 的递归深度以防止大图 DFS 爆栈
sys.setrecursionlimit(300000)

class TwoSat:
    def __init__(self, n):
        """
        初始化 2-SAT 求解器
        :param n: 原始节点的数量 (节点编号从 0 到 n-1)
        """
        self.n = n
        self.num_vars = 2 * n
        self.adj = [[] for _ in range(self.num_vars)]
        self.answer = [0] * n  # 存储最终每个节点的取值选择 (0 或 1)

    def _get_lit(self, u, is_true):
        """
        将 (节点, 布尔状态) 转换为底层的 2-SAT 图节点编号
        """
        return 2 * u + 1 if is_true else 2 * u

    def add_implication(self, u, u_state, v, v_state):
        """
        添加一条蕴含边：如果 u 是 u_state，那么 v 必须是 v_state (u_state -> v_state)
        """
        src = self._get_lit(u, u_state)
        dst = self._get_lit(v, v_state)
        self.adj[src].append(dst)

    def add_clause(self, u, u_state, v, v_state):
        """
        添加一个子句约束。
        配合你原本的代码逻辑：
        如果 choices[vi][i] == choices[vj][j] 发生冲突，说明不能同时选这两者。
        即: not (u == u_state and v == v_state) 
        等价于: (u != u_state) or (v != v_state)
        也就是: (u == u_state ^ 1) or (v == v_state ^ 1)
        
        转换为蕴含式：
        (u == u_state) -> (v == v_state ^ 1)
        (v == v_state) -> (u == u_state ^ 1)
        """
        # 如果 u 满足了冲突状态，则 v 必须避开冲突状态 (走向相反状态)
        self.add_implication(u, u_state, v, v_state ^ 1)
        self.add_implication(v, v_state, u, u_state ^ 1)

    def satisfiable(self):
        """
        使用 Tarjan 算法判断是否有可行解，并构造可行解
        :return: True 如果有解，否则 False
        """
        dfn = [-1] * self.num_vars
        low = [-1] * self.num_vars
        scc_id = [-1] * self.num_vars
        in_stack = [False] * self.num_vars
        stack = []
        
        self.timer = 0
        self.scc_cnt = 0

        # 用迭代/递归形式的 Tarjan。这里给出一个标准的递归 Tarjan。
        # 如果题目点数达到了 10^5 级别，建议用手工栈模拟以绝对避免爆栈。
        def tarjan(u):
            dfn[u] = low[u] = self.timer
            self.timer += 1
            stack.append(u)
            in_stack[u] = True

            for v in self.adj[u]:
                if dfn[v] == -1:
                    tarjan(v)
                    if low[v] < low[u]:
                        low[u] = low[v]
                elif in_stack[v]:
                    if dfn[v] < low[u]:
                        low[u] = dfn[v]

            if low[u] == dfn[u]:
                while True:
                    v = stack.pop()
                    in_stack[v] = False
                    scc_id[v] = self.scc_cnt
                    if v == u:
                        break
                self.scc_cnt += 1

        # 遍历所有底层变量节点跑 Tarjan
        for i in range(self.num_vars):
            if dfn[i] == -1:
                tarjan(i)

        # 检查是否存在强连通矛盾 (一个变量的 True 状态和 False 状态在同一个强连通分量里)
        for i in range(self.n):
            if scc_id[2 * i] == scc_id[2 * i + 1]:
                return False
            
            # Tarjan 算法得出的强连通分量编号是反向拓扑序。
            # 拓扑序越靠后（scc_id 越小）代表越先被缩点，即在原图里属于“因”或位置靠前的点。
            # 2-SAT 的拓扑染色原则：选择拓扑序较后的状态（即 scc_id 较小的状态）
            if scc_id[2 * i] < scc_id[2 * i + 1]:
                self.answer[i] = 0  # 选 False (状态0)
            else:
                self.answer[i] = 1  # 选 True (状态1)

        return True

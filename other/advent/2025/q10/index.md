# 问题来源
https://adventofcode.com/2025/day/10
[整数线性规划问题](<q10 copy 2.py>)

# 整数线性规划 (Integer Linear Programming, ILP) 详解

## 1. 基本概念

### 1.1 定义
**整数线性规划 (ILP)** 是线性规划 (LP) 的扩展，要求部分或全部决策变量取整数值。

标准形式：
\[
\begin{aligned}
\min \quad & \mathbf{c}^T \mathbf{x} \\
\text{s.t.} \quad & A\mathbf{x} \leq \mathbf{b} \\
& \mathbf{x} \geq 0 \\
& x_i \in \mathbb{Z}, \quad \forall i \in I
\end{aligned}
\]
其中 \( I \subseteq \{1, 2, \ldots, n\} \) 是需要整数的变量索引集合。

### 1.2 分类
- **纯整数规划 (Pure ILP)**：所有变量都是整数
- **混合整数规划 (MIP/MILP)**：部分变量是整数，部分是实数
- **0-1整数规划 (Binary ILP)**：变量只能取0或1

## 2. 为什么ILP难解？

### 2.1 与线性规划的比较
| 特性 | 线性规划 (LP) | 整数线性规划 (ILP) |
|------|--------------|-------------------|
| 可行域 | 凸多面体 | 离散点集 |
| 最优解位置 | 顶点 | 可行整数点 |
| 求解方法 | 单纯形法、内点法 | 分支定界、割平面等 |
| 复杂度 | 多项式时间 | NP难问题 |

### 2.2 困难性原因
1. **可行域非凸**：整数点的集合不构成凸集
2. **组合爆炸**：整数点数量可能呈指数增长
3. **间隙 (Integrality Gap)**：整数最优解与线性松弛最优解之间的差距可能很大

## 3. 常用求解算法

### 3.1 分支定界法 (Branch and Bound)
```python
class BranchAndBound:
    """
    分支定界法伪代码结构
    """
    def solve(self, problem):
        # 1. 初始化
        best_solution = None
        best_value = float('inf')
        active_nodes = [root_node]
        
        while active_nodes:
            # 2. 选择节点
            node = self.select_node(active_nodes)
            
            # 3. 求解线性松弛
            relaxed_solution = solve_lp_relaxation(node)
            
            if relaxed_solution is None:
                # 无解，剪枝
                continue
            
            relaxed_value = relaxed_solution.value
            
            # 4. 剪枝条件
            if relaxed_value >= best_value:
                # 界限剪枝
                continue
            
            if is_integer(relaxed_solution):
                # 找到整数解
                if relaxed_value < best_value:
                    best_value = relaxed_value
                    best_solution = relaxed_solution
            else:
                # 5. 分支
                # 选择分数变量进行分支
                branching_var = select_branching_variable(relaxed_solution)
                
                # 创建两个子节点
                node_left = create_node(node, branching_var <= floor(value))
                node_right = create_node(node, branching_var >= ceil(value))
                
                active_nodes.extend([node_left, node_right])
        
        return best_solution
```

### 3.2 割平面法 (Cutting Plane Method)
```python
class CuttingPlane:
    """
    割平面法伪代码
    """
    def solve(self, problem):
        # 1. 求解线性松弛
        current_solution = solve_lp(problem)
        
        while not is_integer(current_solution):
            # 2. 寻找割平面
            cut = find_cutting_plane(current_solution)
            
            if cut is None:
                break  # 找不到割平面
            
            # 3. 添加割平面约束
            problem.add_constraint(cut)
            
            # 4. 重新求解
            current_solution = solve_lp(problem)
        
        return current_solution
```

### 3.3 分支切割法 (Branch and Cut)
结合分支定界和割平面法的优势：
1. 在分支定界的每个节点添加割平面
2. 加速界限收紧，减少分支数量

### 3.4 现代求解器使用的技术
- **预求解 (Presolve)**：简化问题，减少变量和约束
- **启发式方法 (Heuristics)**：快速找到可行解
- **冲突分析 (Conflict Analysis)**：学习约束，避免重复搜索
- **并行计算**：多线程/多进程搜索

## 4. ILP在实际问题中的应用

### 4.1 经典问题
```python
# 背包问题 (0-1 Knapsack)
def knapsack_ilp(weights, values, capacity):
    """
    0-1背包问题的ILP建模
    """
    n = len(weights)
    
    # 决策变量：x_i = 1表示选择物品i
    # 目标：最大化总价值
    # 约束：总重量不超过容量
    # 变量类型：0-1整数
    
    model = ILPModel()
    x = [model.add_binary_var() for _ in range(n)]
    
    # 目标函数
    model.maximize(sum(values[i] * x[i] for i in range(n)))
    
    # 约束
    model.add_constraint(sum(weights[i] * x[i] for i in range(n)) <= capacity)
    
    return model.solve()

# 旅行商问题 (TSP)
def tsp_ilp(distances):
    """
    旅行商问题的ILP建模（DFJ formulation）
    """
    n = len(distances)
    
    # 决策变量：x_ij = 1表示从i到j有边
    # 约束：每个城市一度入、一度出
    # 子回路消除约束
    
    model = ILPModel()
    x = [[model.add_binary_var() for _ in range(n)] for _ in range(n)]
    
    # 目标：最小化总距离
    model.minimize(sum(distances[i][j] * x[i][j] 
                      for i in range(n) for j in range(n) if i != j))
    
    # 度约束
    for i in range(n):
        model.add_constraint(sum(x[i][j] for j in range(n) if j != i) == 1)  # 出度
        model.add_constraint(sum(x[j][i] for j in range(n) if j != i) == 1)  # 入度
    
    # MTZ子回路消除约束（一种简化形式）
    u = [model.add_var(lb=0, ub=n-1, var_type='continuous') for _ in range(n)]
    
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model.add_constraint(u[i] - u[j] + n * x[i][j] <= n - 1)
    
    return model.solve()
```

### 4.2 资源分配问题（如我们讨论的按钮问题）
```python
def button_problem_ilp(targets, buttons):
    """
    按钮问题的ILP建模
    """
    m = len(targets)  # 计数器数量
    n = len(buttons)  # 按钮数量
    
    model = ILPModel()
    
    # 决策变量：每个按钮按下的次数（非负整数）
    x = [model.add_var(lb=0, var_type='integer') for _ in range(n)]
    
    # 约束：每个计数器的总增量等于目标值
    for i in range(m):
        affecting_vars = []
        for j in range(n):
            if i in buttons[j]:
                affecting_vars.append(x[j])
        
        if affecting_vars:
            model.add_constraint(sum(affecting_vars) == targets[i])
    
    # 目标：最小化总按下次数
    model.minimize(sum(x))
    
    return model.solve()
```

## 5. 常用ILP求解器

### 5.1 商业求解器
| 求解器 | 特点 | 许可证 |
|--------|------|--------|
| **Gurobi** | 性能顶尖，用户友好 | 商业，有免费学术版 |
| **CPLEX** | IBM产品，历史悠久 | 商业，有免费学术版 |
| **Xpress** | 欧洲流行，速度快 | 商业 |

### 5.2 开源求解器
| 求解器 | 特点 | 语言 |
|--------|------|------|
| **SCIP** | 混合整数规划，功能强大 | C/C++ |
| **CBC** | COIN-OR项目，基础求解器 | C++ |
| **GLPK** | GNU项目，纯C实现 | C |
| **OR-Tools** | Google开发，包含CP-SAT | C++/Python/Java |

### 5.3 约束规划求解器
| 求解器 | 特点 | 适用问题 |
|--------|------|----------|
| **OR-Tools CP-SAT** | 结合CP和SAT技术 | 组合优化问题 |
| **Chuffed** | 并行求解器 | 约束满足问题 |
| **MiniZinc** | 建模语言+求解器 | 多种优化问题 |

## 6. OR-Tools CP-SAT 详解

### 6.1 为什么CP-SAT适合组合优化问题？
```python
from ortools.sat.python import cp_model

class ButtonProblemSolver:
    def solve_with_cp_sat(self, targets, buttons):
        model = cp_model.CpModel()
        
        # 1. 创建变量
        # CP-SAT支持多种变量类型
        x_vars = []
        for j in range(len(buttons)):
            # 整数变量（非负）
            x = model.NewIntVar(0, 100, f'x_{j}')  # 上界设为100
            
            # 或者使用区间变量
            # x = model.NewIntervalVar(...)
            
            x_vars.append(x)
        
        # 2. 添加约束
        # CP-SAT支持丰富的约束类型
        for i in range(len(targets)):
            affecting = []
            for j, button in enumerate(buttons):
                if i in button:
                    affecting.append(x_vars[j])
            
            if affecting:
                # 线性等式约束
                model.Add(sum(affecting) == targets[i])
                
                # 也可以添加其他约束，如：
                # model.AddMaxEquality(...)  # 最大值约束
                # model.AddAllowedAssignments(...)  # 允许的值组合
        
        # 3. 目标函数
        model.Minimize(sum(x_vars))
        
        # 4. 求解
        solver = cp_model.CpSolver()
        
        # 设置参数
        solver.parameters.max_time_in_seconds = 10
        solver.parameters.num_search_workers = 8  # 并行搜索
        
        # 添加解决方案回调（可选）
        class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
            def __init__(self, variables):
                cp_model.CpSolverSolutionCallback.__init__(self)
                self.__variables = variables
                self.__solution_count = 0
            
            def on_solution_callback(self):
                self.__solution_count += 1
                print(f"Solution {self.__solution_count}:")
                for v in self.__variables:
                    print(f"  {v.Name()} = {self.Value(v)}")
        
        # 求解
        solution_printer = VarArraySolutionPrinter(x_vars)
        status = solver.SolveWithSolutionCallback(model, solution_printer)
        
        if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
            return solver.ObjectiveValue()
        else:
            return None
```

### 6.2 CP-SAT的优势
1. **混合技术**：结合约束规划(CP)、布尔可满足性(SAT)和线性规划(LP)
2. **惰性子句生成**：动态添加约束，避免冗余搜索
3. **对称性检测**：自动识别和利用对称性
4. **并行搜索**：多线程搜索不同区域

## 7. 建模技巧和优化

### 7.1 有效建模原则
1. **选择正确的变量类型**：
   - 小范围整数：`NewIntVar(0, 10, ...)`
   - 0-1变量：`NewBoolVar()`
   - 大范围整数：考虑重新缩放

2. **使用全局约束**：
   ```python
   # 而不是多个单独的约束
   model.AddAllDifferent([x, y, z])  # 全局约束
   
   # 等价于：
   # model.Add(x != y)
   # model.Add(x != z)
   # model.Add(y != z)
   ```

3. **添加冗余约束**：
   ```python
   # 帮助求解器更快收紧界限
   model.Add(sum(x_vars) >= min(targets))
   model.Add(sum(x_vars) <= sum(targets))
   ```

### 7.2 性能优化
```python
def optimize_model(model, x_vars, targets):
    """添加优化约束"""
    # 1. 对称性打破
    # 如果按钮相似，可以排序
    for i in range(len(x_vars) - 1):
        if buttons_are_similar(i, i+1):
            model.Add(x_vars[i] <= x_vars[i+1])
    
    # 2. 上界收紧
    max_presses = sum(targets)
    for x in x_vars:
        model.Add(x <= max_presses)
    
    # 3. 下界估计
    min_presses = estimate_lower_bound(targets, buttons)
    model.Add(sum(x_vars) >= min_presses)
    
    # 4. 启发式变量选择
    # CP-SAT会自动选择，但可以提示
    for x in x_vars:
        model.AddHint(x, initial_guess)  # 提供初始解提示
```

## 8. 实际应用案例

### 8.1 排班问题
```python
def nurse_scheduling():
    """护士排班问题的ILP建模"""
    model = cp_model.CpModel()
    
    # 护士、天数、班次
    nurses = 10
    days = 7
    shifts = 3
    
    # 决策变量：x[n, d, s] = 1表示护士n在第d天上s班次
    x = {}
    for n in range(nurses):
        for d in range(days):
            for s in range(shifts):
                x[(n, d, s)] = model.NewBoolVar(f'x_{n}_{d}_{s}')
    
    # 约束示例：
    # 1. 每个护士每天最多上一个班次
    for n in range(nurses):
        for d in range(days):
            model.Add(sum(x[(n, d, s)] for s in range(shifts)) <= 1)
    
    # 2. 每个班次每天需要至少2名护士
    for d in range(days):
        for s in range(shifts):
            model.Add(sum(x[(n, d, s)] for n in range(nurses)) >= 2)
    
    # 3. 护士连续工作不超过3天
    for n in range(nurses):
        for d in range(days - 3):
            model.Add(sum(x[(n, d + k, s)] 
                         for k in range(4) for s in range(shifts)) <= 3)
    
    # 目标：最小化总班次数
    model.Minimize(sum(x.values()))
    
    return model
```

### 8.2 车辆路径问题
```python
def vehicle_routing(customers, vehicles, capacity):
    """车辆路径问题的ILP建模"""
    model = cp_model.CpModel()
    
    n_customers = len(customers)
    n_vehicles = len(vehicles)
    
    # 决策变量：x[i, j, k] = 1表示车辆k从i行驶到j
    x = {}
    for i in range(n_customers + 1):  # +1 for depot
        for j in range(n_customers + 1):
            for k in range(n_vehicles):
                if i != j:
                    x[(i, j, k)] = model.NewBoolVar(f'x_{i}_{j}_{k}')
    
    # 流平衡约束、容量约束、子回路消除约束等...
    
    # 目标：最小化总行驶距离
    distances = calculate_distances(customers)
    objective_terms = []
    for i in range(n_customers + 1):
        for j in range(n_customers + 1):
            if i != j:
                for k in range(n_vehicles):
                    objective_terms.append(distances[i][j] * x[(i, j, k)])
    
    model.Minimize(sum(objective_terms))
    
    return model
```

## 9. 学习资源

### 9.1 书籍
- 《Integer Programming》by Laurence A. Wolsey
- 《Model Building in Mathematical Programming》by H. Paul Williams
- 《Python for Optimization》by Hans Petter Langtangen

### 9.2 在线课程
- Coursera: Discrete Optimization (University of Melbourne)
- EdX: Optimization Methods in Business Analytics (Georgia Tech)
- MIT OpenCourseWare: Introduction to Mathematical Programming

### 9.3 文档和教程
- OR-Tools官方文档：https://developers.google.com/optimization
- Gurobi优化指南：https://www.gurobi.com/resources/
- CPLEX教程：https://www.ibm.com/docs/en/icos

## 10. 总结

整数线性规划是解决组合优化问题的强大工具。虽然理论上是NP难的，但现代求解器（如OR-Tools CP-SAT）通过结合多种技术，能够高效解决许多实际问题。

**关键要点**：
1. **正确建模**比算法选择更重要
2. **理解问题结构**有助于添加有效约束
3. **预处理和简化**可以显著提高求解速度
4. **不要害怕尝试**不同求解器和参数设置
5. **实际问题中**，通常可以在合理时间内找到高质量解（即使不是理论最优）

对于按钮问题这类资源分配问题，ILP/CP-SAT是最适合的解决方案，因为它能：
1. 保证找到最优解（如果存在）
2. 处理各种约束和变量类型
3. 利用现代求解器的先进技术
4. 提供可扩展的解决方案框架
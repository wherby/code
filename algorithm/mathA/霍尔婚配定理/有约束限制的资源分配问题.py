
# https://codeforces.com/gym/104052/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0214/solution/cf104052b.md

def solve_resource_constraint():
    # 1. 定义资源消耗矩阵 (Rows: 套餐, Cols: 资源)
    # 这里的每一行代表一种套餐，每一列代表一种资源（如杏、蕉、苹、梨）
    costs = [
        [2, 1, 1, 0], # 套餐 A 的资源消耗
        [2, 0, 2, 0], # 套餐 B 的资源消耗
        [1, 1, 2, 1]  # 套餐 C 的资源消耗
    ]
    
    # 2. 读取当前拥有的资源总量
    resources = [A, B, L, P] 
    
    n_resources = len(resources)
    n_sets = len(costs)
    ans = float('inf')
    
    # 3. 二进制枚举资源的所有非空子集 (2^N - 1)
    for i in range(1, 1 << n_resources):
        current_resource_sum = 0
        for j in range(n_resources):
            if (i >> j) & 1:
                current_resource_sum += resources[j]
        
        # 4. 计算在这个资源子集下，每种套餐“最少”贡献了多少消耗
        min_cost_per_set = float('inf')
        for j in range(n_sets):
            set_requirement = 0
            for k in range(n_resources):
                if (i >> k) & 1:
                    set_requirement += costs[j][k]
            
            # 关键：计算每种套餐对当前选定资源集的“有效负担”
            min_cost_per_set = min(min_cost_per_set, set_requirement)
        
        # 5. 更新全局瓶颈
        if min_cost_per_set > 0:
            ans = min(ans, current_resource_sum // min_cost_per_set)
            
    return ans
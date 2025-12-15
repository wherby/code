import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
FILEDEBUG=False

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



ls = []
try:
    with open(filename, 'r') as file:
        for line in file:
            ls.append(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


from ortools.sat.python import cp_model
from typing import List, Tuple, Optional
import sys

class MachineSolver:
    """机器问题求解器"""
    
    def __init__(self, time_limit_seconds: int = 10):
        """
        初始化求解器
        
        参数:
            time_limit_seconds: 每个机器的最大求解时间（秒）
        """
        self.time_limit_seconds = time_limit_seconds
    
    def solve_machine(self, targets: List[int], buttons: List[List[int]]) -> Optional[int]:
        """
        求解单个机器的最小按下次数
        
        参数:
            targets: 每个计数器的目标值列表
            buttons: 按钮列表，每个按钮是它影响的计数器索引列表
        
        返回:
            最小按下次数，如果无解返回 None
        """
        m = len(targets)  # 计数器数量
        n = len(buttons)  # 按钮数量
        
        if m == 0 or n == 0:
            return 0 if all(t == 0 for t in targets) else None
        
        # 创建模型
        model = cp_model.CpModel()
        
        # 1. 创建变量：每个按钮的按下次数
        # 计算合理的上界：最差情况下，每个目标值都单独由一个按钮完成
        # 上界可以设为 max(targets) 或更紧的界限
        max_target = max(targets)
        
        # 为每个按钮创建变量
        x_vars = []
        for j in range(n):
            # 计算这个按钮能影响的计数器的最大目标值
            affected_targets = [targets[i] for i in buttons[j] if i < m]
            if affected_targets:
                # 更紧的上界：按钮最多需要按它所影响计数器的最大目标值那么多次
                upper_bound = max(affected_targets)
            else:
                upper_bound = 0  # 不影响任何计数器
            
            x_var = model.NewIntVar(0, upper_bound, f'x_{j}')
            x_vars.append(x_var)
        
        # 2. 添加约束：每个计数器的总增量必须等于目标值
        # 先建立计数器到按钮的映射
        counter_to_buttons = [[] for _ in range(m)]
        for j, button in enumerate(buttons):
            for i in button:
                if i < m:  # 确保索引有效
                    counter_to_buttons[i].append(j)
        
        # 添加每个计数器的约束
        for i in range(m):
            if targets[i] > 0:
                # 如果目标值>0但没有按钮影响这个计数器，则无解
                if not counter_to_buttons[i]:
                    return None
                
                # 收集影响这个计数器的所有按钮变量
                affecting_vars = [x_vars[j] for j in counter_to_buttons[i]]
                model.Add(sum(affecting_vars) == targets[i])
            elif targets[i] == 0:
                # 目标值为0，所有影响这个计数器的按钮按下次数总和必须为0
                if counter_to_buttons[i]:
                    affecting_vars = [x_vars[j] for j in counter_to_buttons[i]]
                    model.Add(sum(affecting_vars) == 0)
            else:
                # 目标值为负，无解
                return None
        
        # 3. 设置目标函数：最小化总按下次数
        total_presses = sum(x_vars)
        model.Minimize(total_presses)
        
        # 4. 求解
        solver = cp_model.CpSolver()
        
        # 设置求解器参数
        solver.parameters.max_time_in_seconds = self.time_limit_seconds
        solver.parameters.log_search_progress = False
        solver.parameters.num_search_workers = 8  # 使用多核
        
        # 求解
        status = solver.Solve(model)
        
        # 5. 处理结果
        if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
            # 计算总按下次数
            total = int(solver.Value(total_presses))
            
            # 验证解（可选，用于调试）
            if self._verify_solution(targets, buttons, solver, x_vars):
                return total
            else:
                print("Warning: Solution verification failed")
                return None
        else:
            # 无解或超时
            return None
    
    def _verify_solution(self, targets: List[int], buttons: List[List[int]], 
                         solver: cp_model.CpSolver, x_vars: list) -> bool:
        """验证解是否正确"""
        m = len(targets)
        
        # 计算每个计数器的实际值
        actual_counts = [0] * m
        
        for j, x_var in enumerate(x_vars):
            presses = solver.Value(x_var)
            if presses > 0:
                for i in buttons[j]:
                    if i < m:
                        actual_counts[i] += presses
        
        # 检查是否匹配目标值
        for i in range(m):
            if actual_counts[i] != targets[i]:
                print(f"Counter {i}: expected {targets[i]}, got {actual_counts[i]}")
                return False
        
        return True
    
    def solve_all_machines(self, machines: List[Tuple[List[int], List[List[int]]]]) -> Optional[int]:
        """
        求解所有机器的问题
        
        参数:
            machines: 机器列表，每个机器是 (targets, buttons) 元组
        
        返回:
            所有机器的最小按下次数总和，如果任一机器无解则返回 None
        """
        total_presses = 0
        
        print(f"Solving {len(machines)} machines...")
        print("=" * 50)
        
        for idx, (targets, buttons) in enumerate(machines):
            print(f"\nMachine {idx}:")
            print(f"  Counters: {len(targets)}")
            print(f"  Buttons: {len(buttons)}")
            print(f"  Targets: {targets}")
            
            result = self.solve_machine(targets, buttons)
            
            if result is None:
                print(f"  Result: NO SOLUTION")
                return None
            else:
                print(f"  Result: {result} presses")
                total_presses += result
        
        print("\n" + "=" * 50)
        print(f"TOTAL PRESSES: {total_presses}")
        
        return total_presses


    

solver = MachineSolver(time_limit_seconds=5)


def parser(line):
    ls = line.split("]")
    target = ls[0][1:]
    ls = ls[1].split("{")
    ops = ls[0].split(" ")
    ops = [a[1:-1] for a in ops if len(a)>0]
    ops = [list(map(int,a.split(","))) for a in ops]
    val = ls[1]
    val = val[:-1].split(",")
    val = [int(a) for a in val if len(a) >0]
    #print(val,len(ops),ops)
    result = solver.solve_machine(val, ops)
    
    return result


def solve():
    global ls
    sm = 0 
    for line in ls:
        sm+= parser(line)
        #print(target,ops,findMinOps(target,ops))

    print(sm)

    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    
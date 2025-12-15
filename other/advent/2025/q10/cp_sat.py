

"""
使用 Google OR-Tools CP-SAT 求解器解决机器按钮最小按下次数问题
"""

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


def read_input_file(filename: str) -> List[Tuple[List[int], List[List[int]]]]:
    """
    从文件读取输入数据
    
    文件格式：
    第一行：机器数量 N
    对于每个机器：
      第一行：计数器数量 M
      第二行：M 个目标值（空格分隔）
      第三行：按钮数量 B
      接下来 B 行：每行是按钮影响的计数器索引（空格分隔，从0开始）
    """
    machines = []
    
    with open(filename, 'r') as f:
        # 读取机器数量
        num_machines = int(f.readline().strip())
        
        for machine_idx in range(num_machines):
            # 跳过空行
            line = f.readline().strip()
            while line == "":
                line = f.readline().strip()
            
            # 读取计数器数量
            m = int(line)
            
            # 读取目标值
            targets_line = f.readline().strip()
            while targets_line == "":
                targets_line = f.readline().strip()
            targets = list(map(int, targets_line.split()))
            
            if len(targets) != m:
                raise ValueError(f"Machine {machine_idx}: Expected {m} targets, got {len(targets)}")
            
            # 读取按钮数量
            buttons_line = f.readline().strip()
            while buttons_line == "":
                buttons_line = f.readline().strip()
            n = int(buttons_line)
            
            # 读取按钮
            buttons = []
            for button_idx in range(n):
                button_line = f.readline().strip()
                # 如果是空行，按钮不影响任何计数器
                if button_line == "":
                    buttons.append([])
                else:
                    button = list(map(int, button_line.split()))
                    buttons.append(button)
            
            machines.append((targets, buttons))
    
    return machines


def example_problem() -> List[Tuple[List[int], List[List[int]]]]:
    """返回题目中的示例问题"""
    return [
        # 机器1
        (
            [3, 5, 4, 7],
            [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]
        ),
        # 机器2
        (
            [7, 5, 12, 7, 2],
            [[0, 2, 3, 4], [2, 3], [0, 4], [0, 1, 2], [1, 2, 3, 4]]
        ),
        # 机器3
        (
            [10, 11, 11, 5, 10, 5],
            [[0, 1, 2, 3, 4], [0, 3, 4], [0, 1, 2, 4, 5], [1, 2]]
        )
    ]


def test_small_problem():
    """测试一个小问题"""
    # 简单示例：3个计数器，3个按钮
    targets = [2, 3, 1]
    buttons = [
        [0, 1],    # 按钮0影响计数器0和1
        [1, 2],    # 按钮1影响计数器1和2
        [0, 2]     # 按钮2影响计数器0和2
    ]
    
    solver = MachineSolver(time_limit_seconds=5)
    result = solver.solve_machine(targets, buttons)
    
    print(f"Targets: {targets}")
    print(f"Buttons: {buttons}")
    print(f"Minimal presses: {result}")
    
    # 验证：应该可以找到解
    # 可能的解：按钮0按2次，按钮1按1次，按钮2按0次
    # 计数器0: 2 (来自按钮0) + 0 = 2 ✓
    # 计数器1: 2 + 1 = 3 ✓
    # 计数器2: 1 + 0 = 1 ✓
    # 总次数: 3


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Solve machine button pressing problem')
    parser.add_argument('--example', action='store_true', help='Use example problem from description')
    parser.add_argument('--test', action='store_true', help='Test small problem')
    parser.add_argument('--file', type=str, help='Input file path')
    parser.add_argument('--time-limit', type=int, default=10, help='Time limit per machine in seconds')
    
    args = parser.parse_args()
    
    solver = MachineSolver(time_limit_seconds=args.time_limit)
    
    if args.test:
        test_small_problem()
    elif args.example:
        print("Solving example problem from description...")
        machines = example_problem()
        total = solver.solve_all_machines(machines)
        if total is not None:
            print(f"\nExpected total: 10 + 12 + 11 = 33")
            print(f"Computed total: {total}")
    elif args.file:
        print(f"Reading input from {args.file}...")
        try:
            machines = read_input_file(args.file)
            solver.solve_all_machines(machines)
        except FileNotFoundError:
            print(f"Error: File {args.file} not found")
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print("Please specify --example, --test, or --file <filename>")
        print("\nExample usage:")
        print("  python solve_machines.py --example")
        print("  python solve_machines.py --file input.txt")
        print("  python solve_machines.py --test")


if __name__ == "__main__":
    main()
    test_small_problem()
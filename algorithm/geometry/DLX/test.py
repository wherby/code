class DLXNode:
    """Dancing Links节点"""
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.col = None  # 列头节点
        self.row = None  # 行标识符（用于恢复解）
        self.size = 0    # 列的大小（列头节点使用）

class DLXSolver:
    """使用DLX算法解决数独"""
    
    def __init__(self, sudoku_board=None):
        self.sudoku_size = 9
        self.box_size = 3
        self.total_constraints = 4 * self.sudoku_size * self.sudoku_size  # 324
        self.header = None
        self.solution = []
        self.row_info = []  # 记录每行对应的(r, c, num)
        
        if sudoku_board:
            self.load_sudoku(sudoku_board)
    
    def load_sudoku(self, board):
        """加载数独棋盘"""
        if len(board) != self.sudoku_size or any(len(row) != self.sudoku_size for row in board):
            raise ValueError(f"数独必须是{self.sudoku_size}x{self.sudoku_size}")
        
        self.board = [row[:] for row in board]  # 深拷贝
        self.build_matrix()
    
    def build_matrix(self):
        """构建精确覆盖矩阵"""
        # 初始化空矩阵（行列表）
        matrix_rows = []
        self.row_info = []
        
        # 为每个格子的每个可能数字创建行
        for r in range(self.sudoku_size):
            for c in range(self.sudoku_size):
                # 如果格子已经有数字，只创建该数字的行
                if self.board[r][c] != 0:
                    num = self.board[r][c]
                    row = self.create_row(r, c, num)
                    matrix_rows.append(row)
                    self.row_info.append((r, c, num))
                else:
                    # 否则为所有可能数字创建行
                    for num in range(1, 10):
                        row = self.create_row(r, c, num)
                        matrix_rows.append(row)
                        self.row_info.append((r, c, num))
        
        # 转换为0-1矩阵
        self.matrix = matrix_rows
        self.build_dlx()
    
    def create_row(self, r, c, num):
        """创建一行（对应在(r,c)放置数字num）"""
        # 列索引计算
        # 1. 单元格约束: 0-80
        cell_col = r * self.sudoku_size + c
        
        # 2. 行约束: 81-161
        row_col = self.sudoku_size * self.sudoku_size + r * self.sudoku_size + (num - 1)
        
        # 3. 列约束: 162-242
        col_col = 2 * self.sudoku_size * self.sudoku_size + c * self.sudoku_size + (num - 1)
        
        # 4. 宫约束: 243-323
        box_r = r // self.box_size
        box_c = c // self.box_size
        box_col = 3 * self.sudoku_size * self.sudoku_size + (box_r * self.box_size + box_c) * self.sudoku_size + (num - 1)
        
        # 创建行向量（324列）
        row = [0] * self.total_constraints
        row[cell_col] = 1
        row[row_col] = 1
        row[col_col] = 1
        row[box_col] = 1
        
        return row
    
    def build_dlx(self):
        """构建Dancing Links数据结构"""
        if not self.matrix:
            return
        
        num_cols = self.total_constraints
        
        # 创建列头节点
        header = DLXNode()
        col_headers = []
        current = header
        
        for col in range(num_cols):
            col_node = DLXNode()
            col_node.col = col
            col_node.left = current
            current.right = col_node
            current = col_node
            col_headers.append(col_node)
        
        current.right = header
        header.left = current
        
        # 添加行节点
        for row_idx, row in enumerate(self.matrix):
            first_node = None
            prev_node = None
            
            for col_idx, val in enumerate(row):
                if val == 1:
                    col_node = col_headers[col_idx]
                    node = DLXNode()
                    node.row = row_idx
                    node.col = col_node
                    
                    # 插入到列中
                    node.up = col_node.up
                    node.down = col_node
                    col_node.up.down = node
                    col_node.up = node
                    col_node.size += 1
                    
                    # 插入到行中
                    if first_node is None:
                        first_node = node
                        prev_node = node
                        node.left = node
                        node.right = node
                    else:
                        node.left = prev_node
                        node.right = first_node
                        prev_node.right = node
                        first_node.left = node
                        prev_node = node
        
        self.header = header
    
    def cover(self, col_node):
        """覆盖一列"""
        col_node.right.left = col_node.left
        col_node.left.right = col_node.right
        
        row_node = col_node.down
        while row_node != col_node:
            right_node = row_node.right
            while right_node != row_node:
                right_node.down.up = right_node.up
                right_node.up.down = right_node.down
                right_node.col.size -= 1
                right_node = right_node.right
            row_node = row_node.down
    
    def uncover(self, col_node):
        """揭开一列"""
        row_node = col_node.up
        while row_node != col_node:
            left_node = row_node.left
            while left_node != row_node:
                left_node.col.size += 1
                left_node.down.up = left_node
                left_node.up.down = left_node
                left_node = left_node.left
            row_node = row_node.up
        
        col_node.right.left = col_node
        col_node.left.right = col_node
    
    def choose_column(self):
        """选择列大小最小的列（启发式）"""
        chosen = self.header.right
        current = chosen.right
        
        while current != self.header:
            if current.size < chosen.size:
                chosen = current
            current = current.right
        
        return chosen
    
    def search(self, k=0):
        """递归搜索解"""
        if self.header.right == self.header:
            return True
        
        col = self.choose_column()
        if col.size == 0:
            return False
        
        self.cover(col)
        
        row_node = col.down
        while row_node != col:
            self.solution.append(row_node.row)
            
            # 覆盖该行中的其他列
            right_node = row_node.right
            while right_node != row_node:
                self.cover(right_node.col)
                right_node = right_node.right
            
            # 递归搜索
            if self.search(k + 1):
                return True
            
            # 回溯
            self.solution.pop()
            
            # 揭开该行中的其他列
            left_node = row_node.left
            while left_node != row_node:
                self.uncover(left_node.col)
                left_node = left_node.left
            
            row_node = row_node.down
        
        self.uncover(col)
        return False
    
    def solve(self):
        """解数独"""
        if not self.header:
            raise ValueError("请先加载数独棋盘")
        
        self.solution = []
        if self.search():
            # 从解中恢复数独
            result_board = [[0] * self.sudoku_size for _ in range(self.sudoku_size)]
            
            # 首先填入已知数字
            for r in range(self.sudoku_size):
                for c in range(self.sudoku_size):
                    if self.board[r][c] != 0:
                        result_board[r][c] = self.board[r][c]
            
            # 填入DLX找到的解
            for row_idx in self.solution:
                r, c, num = self.row_info[row_idx]
                result_board[r][c] = num
            
            return result_board
        else:
            return None  # 无解
    
    def print_sudoku(self, board):
        """打印数独棋盘"""
        for i, row in enumerate(board):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            row_str = ""
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += "| "
                row_str += (str(num) if num != 0 else ".") + " "
            print(row_str)


# 测试代码
def test_sudoku_solver():
    """测试数独求解器"""
    
    # 测试用例1：简单数独
    easy_sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    # 测试用例2：困难数独
    hard_sudoku = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]
    
    # 测试用例3：空数独（所有解）
    empty_sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    print("=" * 50)
    print("测试简单数独:")
    print("=" * 50)
    print("原始数独:")
    solver = DLXSolver(easy_sudoku)
    solver.print_sudoku(easy_sudoku)
    
    print("\n求解结果:")
    result = solver.solve()
    if result:
        solver.print_sudoku(result)
    else:
        print("无解!")
    
    print("\n" + "=" * 50)
    print("测试困难数独:")
    print("=" * 50)
    print("原始数独:")
    solver2 = DLXSolver(hard_sudoku)
    solver2.print_sudoku(hard_sudoku)
    
    print("\n求解结果:")
    result2 = solver2.solve()
    if result2:
        solver2.print_sudoku(result2)
    else:
        print("无解!")
    
    print("\n" + "=" * 50)
    print("测试空数独（将找到一个解）:")
    print("=" * 50)
    print("原始数独（全空）:")
    solver3 = DLXSolver(empty_sudoku)
    solver3.print_sudoku(empty_sudoku)
    
    print("\n求解结果:")
    result3 = solver3.solve()
    if result3:
        solver3.print_sudoku(result3)
    else:
        print("无解!")

# 更简洁的使用示例
def quick_example():
    """快速使用示例"""
    # 创建一个数独
    sudoku = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]
    
    print("数独求解示例:")
    print("-" * 30)
    
    # 创建求解器
    solver = DLXSolver(sudoku)
    
    print("输入数独:")
    for row in sudoku:
        print(" ".join(str(x) if x != 0 else "." for x in row))
    
    print("\n求解中...")
    
    # 求解
    solution = solver.solve()
    
    if solution:
        print("\n解:")
        for row in solution:
            print(" ".join(str(x) for x in row))
    else:
        print("\n无解!")

# 性能测试
def performance_test():
    """性能测试"""
    import time
    
    # 使用世界最难的数独之一
    world_hardest = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]
    
    print("性能测试: 世界最难数独")
    print("-" * 40)
    
    start_time = time.time()
    solver = DLXSolver(world_hardest)
    solution = solver.solve()
    end_time = time.time()
    
    if solution:
        print(f"求解成功! 耗时: {end_time - start_time:.4f}秒")
        print("\n解的前3行:")
        for i in range(3):
            print(" ".join(str(x) for x in solution[i]))
    else:
        print("无解!")

if __name__ == "__main__":
    print("DLX数独求解器")
    print("=" * 60)
    
    # 运行快速示例
    quick_example()
    
    print("\n" + "=" * 60)
    
    # 运行完整测试
    test_sudoku_solver()
    
    print("\n" + "=" * 60)
    
    # 运行性能测试
    performance_test()
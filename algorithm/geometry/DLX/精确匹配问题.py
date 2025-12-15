# 精确把物品填满区域
from collections import defaultdict
import sys

class DLXNode:
    """Dancing Links节点"""
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.col = None  # 列头节点
        self.row = None  # 行标识符（放置ID）
        self.size = 0    # 列的大小（列头节点使用）

def parse_input(input_text):
    """解析输入"""
    lines = [line.rstrip('\n') for line in input_text.strip().split('\n')]
    shapes = {}
    regions = []
    
    i = 0
    # 解析形状
    while i < len(lines) and lines[i] and ':' in lines[i] and 'x' not in lines[i]:
        idx = int(lines[i].split(':')[0].strip())
        shape_lines = []
        i += 1
        
        while i < len(lines) and lines[i] and ':' not in lines[i] and 'x' not in lines[i]:
            shape_lines.append(lines[i])
            i += 1
        
        # 转换为坐标集合
        points = []
        for r, row in enumerate(shape_lines):
            for c, ch in enumerate(row):
                if ch == '#':
                    points.append((r, c))
        shapes[idx] = points
        
        # 跳过空行
        while i < len(lines) and (not lines[i] or lines[i].isspace()):
            i += 1
    
    # 解析区域
    while i < len(lines):
        if lines[i] and 'x' in lines[i]:
            line = lines[i].strip()
            parts = line.split(':')
            dim_part = parts[0].strip()
            
            if len(parts) > 1:
                counts = list(map(int, parts[1].strip().split()))
            else:
                counts = []
            
            w, h = map(int, dim_part.split('x'))
            regions.append((w, h, counts))
        i += 1
    
    return shapes, regions

def normalize_shape(shape):
    """规范化形状（移动到原点）"""
    if not shape:
        return tuple()
    min_r = min(r for r, _ in shape)
    min_c = min(c for _, c in shape)
    return tuple(sorted((r - min_r, c - min_c) for r, c in shape))

def generate_orientations(shape):
    """生成形状的所有唯一方向"""
    orientations = set()
    points = list(shape)
    
    # 4种旋转
    for rot in range(4):
        # 旋转
        rotated = points
        for _ in range(rot):
            rotated = [(-y, x) for x, y in rotated]
        
        # 不翻转
        orientations.add(normalize_shape(rotated))
        
        # 水平翻转
        flipped = [(-x, y) for x, y in rotated]
        orientations.add(normalize_shape(flipped))
    
    return [list(orient) for orient in orientations]

class DLXSolver:
    """使用DLX解决包装问题"""
    
    def __init__(self, width, height, shapes_data):
        """
        shapes_data: {shape_id: (count, orientations)}
        """
        self.width = width
        self.height = height
        self.shapes_data = shapes_data
        self.total_cells = width * height
        
        # 生成所有可能的放置
        self.placements = []  # 每个放置：(shape_id, mask, cells)
        self.build_placements()
        
        # 构建DLX矩阵
        self.matrix = self.build_matrix()
        self.header = self.build_dlx()
        
    def build_placements(self):
        """生成所有可能的形状放置"""
        self.placements = []
        
        for shape_id, (count, orientations) in self.shapes_data.items():
            if count <= 0:
                continue
                
            for orient in orientations:
                # 计算边界
                if not orient:
                    continue
                max_r = max(r for r, _ in orient)
                max_c = max(c for _, c in orient)
                h, w = max_r + 1, max_c + 1
                
                # 生成所有位置
                for r in range(self.height - h + 1):
                    for c in range(self.width - w + 1):
                        cells = []
                        mask = 0
                        for dr, dc in orient:
                            cell_r = r + dr
                            cell_c = c + dc
                            cell_idx = cell_r * self.width + cell_c
                            cells.append((cell_r, cell_c))
                            mask |= 1 << cell_idx
                        
                        self.placements.append((shape_id, mask, cells))
    
    def build_matrix(self):
        """构建精确覆盖矩阵"""
        # 列设计：
        # 第1部分：每个形状必须放置指定次数（每个形状有count列）
        # 第2部分：每个棋盘格子最多被占据一次
        
        # 计算总列数
        shape_cols = 0
        for shape_id, (count, _) in self.shapes_data.items():
            shape_cols += count  # 每个形状需要count列
        
        cell_cols = self.total_cells
        total_cols = shape_cols + cell_cols
        
        # 构建矩阵
        matrix = []
        self.placement_info = []  # 记录每行对应的放置信息
        
        # 为每个放置创建行
        row_idx = 0
        shape_col_offset = {}
        
        # 首先计算每个形状的列偏移
        current_col = 0
        for shape_id, (count, _) in self.shapes_data.items():
            if count > 0:
                shape_col_offset[shape_id] = current_col
                current_col += count
        
        # 创建矩阵行
        for shape_id, mask, cells in self.placements:
            for shape_copy in range(self.shapes_data[shape_id][0]):
                row = [0] * total_cols
                
                # 设置形状约束列
                col_idx = shape_col_offset[shape_id] + shape_copy
                row[col_idx] = 1
                
                # 设置格子约束列
                for r, c in cells:
                    cell_idx = shape_cols + r * self.width + c
                    row[cell_idx] = 1
                
                matrix.append(row)
                self.placement_info.append((shape_id, mask, cells))
        
        return matrix
    
    def build_dlx(self):
        """构建Dancing Links数据结构"""
        if not self.matrix:
            return None
            
        num_cols = len(self.matrix[0])
        
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
        
        return header
    
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
        """选择列大小最小的列"""
        chosen = self.header.right
        current = chosen.right
        
        while current != self.header:
            if current.size < chosen.size:
                chosen = current
            current = current.right
        
        return chosen
    
    def search(self, solution, limit=None):
        """递归搜索解"""
        if self.header.right == self.header:
            return True
        
        col = self.choose_column()
        if col.size == 0:
            return False
        
        self.cover(col)
        
        row_node = col.down
        while row_node != col:
            solution.append(row_node.row)
            
            # 覆盖该行中的其他列
            right_node = row_node.right
            while right_node != row_node:
                self.cover(right_node.col)
                right_node = right_node.right
            
            # 递归搜索
            if self.search(solution, limit):
                return True
            
            # 回溯
            solution.pop()
            
            # 揭开该行中的其他列
            left_node = row_node.left
            while left_node != row_node:
                self.uncover(left_node.col)
                left_node = left_node.left
            
            row_node = row_node.down
        
        self.uncover(col)
        return False
    
    def solve(self):
        """求解包装问题"""
        solution = []
        if self.search(solution):
            # 验证解决方案
            used_shapes = defaultdict(int)
            for row_idx in solution:
                shape_id, _, _ = self.placement_info[row_idx]
                used_shapes[shape_id] += 1
            
            # 检查每个形状是否使用了正确数量
            for shape_id, (count, _) in self.shapes_data.items():
                if used_shapes[shape_id] != count:
                    return False
            return True
        return False

def can_fit_with_dlx(width, height, counts, shape_orientations):
    """使用DLX检查是否可以放置所有形状"""
    # 准备形状数据
    shapes_data = {}
    for shape_id, count in enumerate(counts):
        if count > 0 and shape_id < len(shape_orientations) and shape_orientations[shape_id]:
            shapes_data[shape_id] = (count, shape_orientations[shape_id])
    
    if not shapes_data:
        return True
    
    # 快速检查：总面积
    total_cells = 0
    for shape_id, (count, orientations) in shapes_data.items():
        if orientations:
            total_cells += len(orientations[0]) * count
    
    if total_cells > width * height:
        return False
    
    # 使用DLX求解
    solver = DLXSolver(width, height, shapes_data)
    return solver.solve()

def solve(input_text):
    """主求解函数"""
    shapes, regions = parse_input(input_text)
    
    # 预计算所有形状的方向
    max_shape_id = max(shapes.keys()) if shapes else -1
    shape_orientations = [None] * (max_shape_id + 1)
    
    for shape_id, points in shapes.items():
        orientations = generate_orientations(points)
        if orientations:
            # 去重
            unique = []
            seen = set()
            for orient in orientations:
                key = tuple(orient)
                if key not in seen:
                    seen.add(key)
                    unique.append(orient)
            shape_orientations[shape_id] = unique
    
    count_fittable = 0
    results = []
    
    for i, (width, height, counts) in enumerate(regions):
        print(f"处理区域 {i+1}/{len(regions)}: {width}x{height}...", end="")
        
        # 确保counts长度足够
        if len(counts) <= max_shape_id:
            counts = counts + [0] * (max_shape_id + 1 - len(counts))
        
        if can_fit_with_dlx(width, height, counts, shape_orientations):
            count_fittable += 1
            results.append(True)
            print(" 可以")
        else:
            results.append(False)
            print(" 不可以")
    
    return count_fittable, results

# 测试示例
example_input = """0:
###
##.
###

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

3x5: 1 0 0 1 0 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            input_text = f.read()
        count_fittable, _ = solve(input_text)
        print(f"\n可以容纳所有礼物的区域数量: {count_fittable}")
    else:
        print("运行示例...")
        count_fittable, results = solve(example_input)
        print(f"\n可以容纳所有礼物的区域数量: {count_fittable}")
        print("\n详细结果:")
        shapes, regions = parse_input(example_input)
        for i, ((w, h, counts), result) in enumerate(zip(regions, results)):
            status = "可以" if result else "不可以"
            print(f"区域 {i+1}: {w}x{h}, 形状计数 {counts} - {status}容纳所有礼物")
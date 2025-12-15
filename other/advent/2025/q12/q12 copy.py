import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input.txt"
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

from functools import lru_cache
from itertools import product
from collections import defaultdict
import sys

def parse_input(input_text):
    lines = input_text.strip().split('\n')
    shapes = {}
    regions = []
    
    i = 0
    # 解析形状
    while i < len(lines) and lines[i].strip() and ':' in lines[i]:
        idx = int(lines[i].split(':')[0])
        shape_lines = []
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i][0].isdigit():
            shape_lines.append(lines[i].strip())
            i += 1
        
        # 将形状转换为坐标集合
        points = set()
        for r, row in enumerate(shape_lines):
            for c, ch in enumerate(row):
                if ch == '#':
                    points.add((r, c))
        
        shapes[idx] = points
        # 跳过可能的空行
        while i < len(lines) and not lines[i].strip():
            i += 1
    
    # 解析区域
    while i < len(lines):
        line = lines[i].strip()
        if line:
            if ':' in line:
                # 处理区域行
                parts = line.split(':')
                dim_part = parts[0].strip()
                counts_part = parts[1].strip() if len(parts) > 1 else ""
            else:
                dim_part = line
                counts_part = ""
            
            if 'x' in dim_part:
                dims = dim_part.split('x')
                w, h = int(dims[0]), int(dims[1])
                counts = list(map(int, counts_part.split())) if counts_part else []
                regions.append((w, h, counts))
        i += 1
    
    return shapes, regions

def generate_rotations_and_flips(shape_points):
    """生成形状的所有旋转和翻转变体"""
    variants = set()
    
    for flip_h in [False, True]:
        for flip_v in [False, True]:
            for rotation in [0, 1, 2, 3]:  # 0, 90, 180, 270度
                points = shape_points
                
                # 旋转
                for _ in range(rotation):
                    points = {(-y, x) for x, y in points}
                
                # 翻转
                if flip_h:
                    points = {(-x, y) for x, y in points}
                if flip_v:
                    points = {(x, -y) for x, y in points}
                
                # 规范化：移动到原点
                min_r = min(r for r, _ in points)
                min_c = min(c for _, c in points)
                points = {(r - min_r, c - min_c) for r, c in points}
                
                # 转换为排序的元组以便哈希
                variant = tuple(sorted(points))
                variants.add(variant)
    
    return [set(v) for v in variants]

def can_fit_region(shapes, region_width, region_height, counts):
    """检查是否可以在区域中放置所有要求的形状"""
    
    # 预计算每个形状的所有变体
    shape_variants = {}
    for idx, points in shapes.items():
        shape_variants[idx] = generate_rotations_and_flips(points)
    
    # 为每个形状生成所有可能的放置位置
    placements = defaultdict(list)  # shape_idx -> list of (positions set, width, height)
    
    for shape_idx, variants in shape_variants.items():
        for variant in variants:
            # 计算变体的边界
            max_r = max(r for r, _ in variant)
            max_c = max(c for _, c in variant)
            h, w = max_r + 1, max_c + 1
            
            # 生成所有可能的位置
            for start_r in range(region_height - h + 1):
                for start_c in range(region_width - w + 1):
                    # 将形状放置在此位置
                    positions = {(start_r + r, start_c + c) for r, c in variant}
                    placements[shape_idx].append(positions)
    
    # 准备回溯搜索
    board = [[0 for _ in range(region_width)] for _ in range(region_height)]
    
    # 创建形状列表，按大小排序（大的先尝试）
    piece_list = []
    for shape_idx, count in enumerate(counts):
        piece_list.extend([shape_idx] * count)
    
    if not piece_list:
        return True  # 没有形状需要放置
    
    # 按形状大小排序（使用最大变体的大小）
    def get_shape_size(idx):
        max_size = 0
        for variant in shape_variants[idx]:
            max_size = max(max_size, len(variant))
        return max_size
    
    piece_list.sort(key=lambda x: get_shape_size(x), reverse=True)
    
    # 将列表转换为计数字典以便快速检查
    from collections import Counter
    piece_counter = Counter(piece_list)
    
    # 使用记忆化和剪枝的回溯
    @lru_cache(maxsize=None)
    def backtrack(board_state, remaining_counts_tuple):
        # board_state: 压缩的棋盘状态
        # remaining_counts_tuple: 每个形状剩余数量的元组
        
        if all(c == 0 for c in remaining_counts_tuple):
            return True
        
        # 转换为列表以便修改
        remaining_counts = list(remaining_counts_tuple)
        
        # 找到第一个还有剩余的形状
        next_shape = None
        for i, cnt in enumerate(remaining_counts):
            if cnt > 0:
                next_shape = i
                break
        
        if next_shape is None:
            return True
        
        # 解压缩棋盘状态
        board_bits = board_state
        occupied = set()
        for r in range(region_height):
            for c in range(region_width):
                if board_bits & (1 << (r * region_width + c)):
                    occupied.add((r, c))
        
        # 尝试放置这个形状的每个可能位置
        for placement in placements[next_shape]:
            # 检查是否与已放置的形状冲突
            conflict = False
            for pos in placement:
                if pos in occupied:
                    conflict = True
                    break
            
            if not conflict:
                # 放置这个形状
                new_occupied = occupied | placement
                # 创建新的棋盘状态
                new_board_state = 0
                for r, c in new_occupied:
                    new_board_state |= 1 << (r * region_width + c)
                
                # 更新剩余计数
                new_remaining_counts = list(remaining_counts)
                new_remaining_counts[next_shape] -= 1
                
                if backtrack(new_board_state, tuple(new_remaining_counts)):
                    return True
        
        return False
    
    # 初始状态
    initial_board_state = 0
    initial_counts = tuple(counts)
    
    return backtrack(initial_board_state, initial_counts)

# def solve(input_text):
#     shapes, regions = parse_input(input_text)
    
#     count_fittable = 0
#     results = []
    
#     for w, h, counts in regions:
#         # 确保counts长度与形状数量匹配
#         if len(counts) < len(shapes):
#             counts = counts + [0] * (len(shapes) - len(counts))
#         elif len(counts) > len(shapes):
#             counts = counts[:len(shapes)]
        
#         if can_fit_region(shapes, w, h, counts):
#             count_fittable += 1
#             results.append(True)
#         else:
#             results.append(False)
    
#     return count_fittable, results

# # 测试示例输入
# example_input = """0:
# ###
# ##.
# ##.

# 1:
# ###
# ##.
# .##

# 2:
# .##
# ###
# ##.

# 3:
# ##.
# ###
# ##.

# 4:
# ###
# #..
# ###

# 5:
# ###
# .#.
# ###

# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2"""

# if __name__ == "__main__":
#     # 使用示例或从文件读取
#     if len(sys.argv) > 1:
#         with open(sys.argv[1], 'r') as f:
#             input_text = f.read()
#     else:
#         input_text = example_input
    
#     count_fittable, results = solve(input_text)
#     print(f"可以容纳所有礼物的区域数量: {count_fittable}")
    
#     # 打印详细结果
#     shapes, regions = parse_input(input_text)
#     print("\n详细结果:")
#     for i, ((w, h, counts), result) in enumerate(zip(regions, results)):
#         status = "可以" if result else "不能"
#         print(f"区域 {i+1}: {w}x{h}, 形状计数 {counts} - {status}容纳所有礼物")

shapes = {}
def parseShap(lines):
    global shapes
    i = 0
    # 解析形状
    while i < len(lines) and lines[i].strip() and ':' in lines[i]:
        idx = int(lines[i].split(':')[0])
        shape_lines = []
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i][0].isdigit():
            shape_lines.append(lines[i].strip())
            i += 1
        
        # 将形状转换为坐标集合
        points = set()
        for r, row in enumerate(shape_lines):
            for c, ch in enumerate(row):
                if ch == '#':
                    points.add((r, c))
        
        shapes[idx] = points
        # 跳过可能的空行
        while i < len(lines) and not lines[i].strip():
            i += 1

def parseRegion(lines):
    regions=[]
    i= 0
    while i < len(lines):
        line = lines[i].strip()
        if line:
            if ':' in line:
                # 处理区域行
                parts = line.split(':')
                dim_part = parts[0].strip()
                counts_part = parts[1].strip() if len(parts) > 1 else ""
            else:
                dim_part = line
                counts_part = ""
            
            if 'x' in dim_part:
                dims = dim_part.split('x')
                w, h = int(dims[0]), int(dims[1])
                counts = list(map(int, counts_part.split())) if counts_part else []
                regions.append((w, h, counts))
        i += 1
    #print(regions,lines)
    return regions

def solve():
    global ls
    lls = []
    tmp=[]
    for a in ls:
        if len(a)>0:
            tmp.append(a)
        else:
            lls.append(tmp)
            tmp = [] 
    lls.append(tmp)
    for i in range(6):
        parseShap(lls[i])
    regions = parseRegion(lls[6])
    print(lls,shapes,regions)
    count_fittable = 0
    results = []

    for w, h, counts in regions:
        # 确保counts长度与形状数量匹配
        if len(counts) < len(shapes):
            counts = counts + [0] * (len(shapes) - len(counts))
        elif len(counts) > len(shapes):
            counts = counts[:len(shapes)]
    
        if can_fit_region(shapes, w, h, counts):
            count_fittable += 1
            results.append(True)
        else:
            results.append(False)
    print(count_fittable,results)
    return count_fittable, results

    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    
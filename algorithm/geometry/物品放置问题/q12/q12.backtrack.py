# https://adventofcode.com/2025/day/12
from functools import lru_cache
from collections import defaultdict
import sys



def normalize_shape(points):
    """规范化形状（移动到原点）"""
    if not points:
        return []
    min_r = min(r for r, _ in points)
    min_c = min(c for _, c in points)
    return tuple(sorted((r - min_r, c - min_c) for r, c in points))

def generate_all_orientations(shape):
    """生成所有唯一方向（去除重复）"""
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
        
        # 翻转（只需要一种翻转，因为翻转+旋转可以生成所有对称）
        flipped = [(-x, y) for x, y in rotated]  # 水平翻转
        orientations.add(normalize_shape(flipped))
    
    return [list(orient) for orient in orientations]

def get_placements(orientations, width, height):
    """获取形状的所有可能放置位置"""
    placements = []
    
    for orient in orientations:
        # 计算边界
        if not orient:
            continue
        max_r = max(r for r, _ in orient)
        max_c = max(c for _, c in orient)
        h, w = max_r + 1, max_c + 1
        
        # 生成所有位置
        for r in range(height - h + 1):
            for c in range(width - w + 1):
                # 计算占用格子的位掩码
                mask = 0
                for dr, dc in orient:
                    cell_r = r + dr
                    cell_c = c + dc
                    bit_pos = cell_r * width + cell_c
                    mask |= 1 << bit_pos
                placements.append(mask)
    #print(placements,bin(placements[-1]))
    return placements

def solve_region_fast(width, height, counts, shape_placements):
    """使用优化的回溯算法解决区域"""
    total_cells = width * height
    
    # 将形状列表展开
    pieces = []
    for shape_id, count in enumerate(counts):
        if count > 0 and shape_id < len(shape_placements):
            pieces.extend([shape_id] * count)
    
    if not pieces:
        return True
    
    # 按大小排序（大的先放）
    def piece_size(piece_id):
        # 使用第一个放置的大小（所有放置大小相同）
        if shape_placements[piece_id]:
            mask = shape_placements[piece_id][0]
            return bin(mask).count('1')
        return 0
    
    pieces.sort(key=piece_size, reverse=True)
    
    # 预计算每个形状的放置
    placements_by_shape = shape_placements
    
    @lru_cache(maxsize=None)
    def backtrack(piece_idx, board_mask):
        """回溯搜索"""
        if piece_idx >= len(pieces):
            return True
        
        shape_id = pieces[piece_idx]
        
        # 尝试所有可能的放置
        for placement_mask in placements_by_shape[shape_id]:
            # 检查是否与已放置的形状冲突
            if board_mask & placement_mask:
                continue
            
            # 放置形状
            new_mask = board_mask | placement_mask
            
            # 递归
            if backtrack(piece_idx + 1, new_mask):
                return True
        
        return False
    
    return backtrack(0, 0)

def can_fit_region_optimized(width, height, counts, shape_orientations):
    """优化的区域检查"""
    # 快速检查：总面积
    total_required = 0
    for shape_id, count in enumerate(counts):
        if count > 0 and shape_id < len(shape_orientations) and shape_orientations[shape_id]:
            # 使用第一个方向的大小
            total_required += len(shape_orientations[shape_id][0]) * count
    
    if total_required > width * height:
        return False

    # 预计算每个形状的所有放置
    shape_placements = []
    for shape_id in range(len(shape_orientations)):
        if shape_id < len(shape_orientations) and shape_orientations[shape_id]:
            placements = get_placements(shape_orientations[shape_id], width, height)
            if placements:
                # 去重
                unique_placements = []
                seen = set()
                for mask in placements:
                    if mask not in seen:
                        seen.add(mask)
                        unique_placements.append(mask)
                shape_placements.append(unique_placements)
            else:
                shape_placements.append([])
        else:
            shape_placements.append([])
    
    return solve_region_fast(width, height, counts, shape_placements)


    
   




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
     # 预计算所有形状的方向
    max_shape_id = max(shapes.keys()) if shapes else -1
    shape_orientations = [None] * (max_shape_id + 1)
    
    for shape_id, points in shapes.items():
        orientations = generate_all_orientations(points)
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
        
        if can_fit_region_optimized(width, height, counts, shape_orientations):
            count_fittable += 1
            results.append(True)
            print(" 可以")
        else:
            results.append(False)
            print(" 不可以")
    print(count_fittable,results)
    return count_fittable, results

solve()
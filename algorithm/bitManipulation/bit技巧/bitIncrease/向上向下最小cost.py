# https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/
# 把原题的每次操作改为可以任意选择增加1 或者减少1 ，加入了减少1 的时候的最小操作数的判断
def solve(nums, k, m):
    # 我们需要记录当前这 m 个数已经被修改到了什么值
    # 或者更简单的：由于我们要最大化 AND，我们可以直接维护这 m 个数
    # 为了简化，我们每次都重新计算所有数达到 target 的最小代价
    
    ans = 0
    for j in range(30, -1, -1):
        target = ans | (1 << j)
        costs = []
        
        for x in nums:
            # 计算 x 变成任何一个 [满足 target 模式] 的数所需的最小步数
            costs.append(get_min_cost(x, target))
        
        costs.sort()
        # 只要目前最小的 m 个数能在总共 k 步内达到 target
        if sum(costs[:m]) <= k:
            ans = target
            
    return ans

def get_min_cost(x, target):
    if (x & target) == target:
        return 0
    
    # 找到 target 中 x 缺失的最高位 h
    diff = target & ~x
    h = diff.bit_length() - 1
    
    # --- 向上找 (x_up) ---
    # 高位保留, h位变1, 低位按 target 补全（target 低位必须为1的就为1，其余为0以求最小）
    x_up = ((x >> (h + 1)) << (h + 1)) | (1 << h) | (target & ((1 << h) - 1))
    cost_up = x_up - x
    
    # --- 向下找 (x_down) ---
    cost_down = float('inf')
    p = h + 1
    # 向上寻找第一个能借位的点：x[p]==1 且 target[p]==0
    while (1 << p) <= max(x, target): 
        bit = 1 << p
        if (x & bit) and not (target & bit):
            # 构造最大的 x_down：p位变0, 高位保留, 低位在满足 target 前提下全填1
            # 这里的 (bit - 1) 保证了低位所有能填 1 的地方都填了 1
            x_down = ((x >> (p + 1)) << (p + 1)) | (bit - 1)
            # 既然 p > h，x_down 的第 h 位一定是 1，且低位所有 target 的 1 都能保留
            cost_down = x - x_down
            break 
        p += 1
        
    return min(cost_up, cost_down)
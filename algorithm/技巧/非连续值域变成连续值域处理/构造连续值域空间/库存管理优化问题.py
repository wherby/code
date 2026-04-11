# https://codeforces.com/gym/106007/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0409/solution/cf106007c.md
# 使用了空间换时间的技巧，节约了二分查找的复杂度 algorithm/codeforce/docs/空间换时间技巧.md
# 由于d不满足二分条件，不是单调的，所以需要枚举，由于枚举的时候是调和级数所以枚举的时间复杂度是可以接受的
# 而采用了空间换时间的技巧，使得复杂度就是调和级数
# 在找pos的时候，要确定这个pos能被满足，否则当前d就不能使用。 while else： 在while里没有break 就会执行else
# 
# for d in range(1, m + 1): # 枚举补货阈值 d
    # pt = 0 # 当前处理到的客户下标
    # while pt < n:
    #     # 计算从当前客户 pt 开始，最多能消耗多少披萨而不触发补货
    #     # 允许消耗量 = m - d。所以我们要找总消耗量超过 acc[pt] + (m - d) 的第一个位置
    #     # acc[pt] + m - d + 1 就是触发“补货阈值”或“库存不足”的临界点
    #     pos = vis[fmin(total, acc[pt] + m - d + 1)] + 1
        
    #     # 核心检查：如果当前这一段的需求 acc[pos] - acc[pt] 超过了最大库存 m
    #     # 说明即便补满到 m，也无法满足从 pt 到 pos 之间的客户
    #     if m < acc[pos] - acc[pt]: break 
        
    #     pt = pos # 跳跃到下一段
    # else:
    #     # 如果顺利跳出 while（即 pt >= n），说明当前 d 合法
    #     outs.append(d)
    #     break




import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        nums = LII()
    
        total = sum(nums)
        vis = [-1] * (total + 1)
        
        cur = 0
        for i in range(n):
            for j in range(cur + 1, cur + nums[i] + 1):
                vis[j] = i
            cur += nums[i]
        
        acc = list(accumulate(nums, initial=0))
        
        for d in range(1, m + 1):
            pt = 0
            
            while pt < n:
                pos = vis[fmin(total, acc[pt] + m - d + 1)] + 1
                if m < acc[pos] - acc[pt]: break
                pt = pos
            else:
                outs.append(d)
                break
    
    print('\n'.join(map(str, outs)))
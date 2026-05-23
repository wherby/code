# https://codeforces.com/gym/106527/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0520/solution/cf106527c.md
# algorithm/codeforce/docs/hall定理.md 
# 已知所有题目的回答情况，求大于自己分数的最少人数的人数数量
# 这里采用了空位视角，空位数量《超过自己的人产生的数量 + 等于自己的人产生空位的数量
# 假设等于自己的人的空位为v个人，则超过自己的人的数量为n-v
# (i * n - cur_sum) // (i - x) 表示当前有多少空位，和至少要多少等于自己的人才能填补这些空位，
# 找到所有情况的最小值就是最大的可能值？
# 因为我们需要找到最多的普通人，所以对于空位应该从少到多排列






import init_setting
from cflibs import *

def main():  
    t = II()
    outs = []
    
    for _ in range(t):
        n, p, x = MII() # n: 对手人数, p: 题目总数, x: 你做的题数
        nums = LII()    # 长度为 p 的数组，nums[i] 表示第 i 道题被多少个对手做出
        
        # 1. 计数排序：我们要从大到小排列。
        # 题目最多被 n 个对手做出来，所以开 n + 1 的桶
        cnt = [0] * (n + 1)
        for v in nums:
            cnt[v] += 1
        
        sorted_nums = []
        # 从 n 到 0 倒序收集，直接得到从大到小的排序
        for score in range(n, -1, -1):
            for _ in range(cnt[score]):
                sorted_nums.append(score)
        
        # 2. 线性扫描统计前缀和，并利用 Hall 定理更新 v (做题 <= x 的对手人数) 的上界
        cur_sum = 0
        max_v = n # v 的初始最大可能值是总对手人数 n
        
        # i 代表题目子集大小，从 1 到 p (题目总数)
        for i in range(1, p + 1):
            cur_sum += sorted_nums[i - 1] # 此时 i-1 绝对不会超过 p-1，绝不越界
            
            # 只有当题目数量 i > x 时，才会对 v 产生限制
            if i > x:
                # v <= (i * n - S_i) // (i - x)
                limit = (i * n - cur_sum) // (i - x)
                if limit < max_v:
                    max_v = limit
        
        # max_v 至少为 0（即没有对手做题不超过 x）
        max_v = max(max_v, 0)
        
        # 最终要求的是做题严格超过 x 题的对手人数
        # 总对手数 n - 做题不超过 x 的对手数 max_v
        outs.append(n - max_v)
        
    print('\n'.join(map(str, outs)))

main()
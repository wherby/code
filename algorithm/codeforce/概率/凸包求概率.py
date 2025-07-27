# https://codeforces.com/problemset/problem/97/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0726/solution/cf97c.md
# 所有（x,y)概率构成的图像是一个凸包，求y在x的均值为1/2的时候的最大值
# 坐标系变换把1/2的限制，变化到新的坐标系，x==0的时候，y的最大值就是答案
# 坐标系变换 ：algorithm/codeforce/概率/凸包求概率/坐标系变换.png


import init_setting
from cflibs import *
def main():
    n = II()  # 读取整数 n (团队成员数量)
    nums = LFI() # 读取列表 nums，其中 nums[i] 对应于 p_i (i 名老选手时的获奖概率)
    
    # 初始化答案为当平均 a_k = n // 2 时的概率。
    # 如果 n 是偶数，n // 2 正好是一个可能的 a_i 值。
    # 如果 n 是奇数，n // 2 会向下取整，例如 n=5, n//2=2。
    # 这个初始值是基于一种简单的猜测，即最优解可能出现在 a_k 接近 n/2 的情况。
    ans = nums[n // 2] 
    
    # 双重循环遍历所有可能的 (i, p_i) 和 (j, p_j) 点对
    for i in range(n + 1):
        # wi 和 wj 的定义是 2 * a_k - n。
        # 这里的 wi 和 wj 实际上是在调整坐标系，或者说在考虑一个加权平均的特殊形式。
        # 长期来看，我们有平均 a_k <= n/2，这意味着 2 * 平均 a_k - n <= 0。
        # 因此，我们需要在新的坐标系下找到一个横坐标 <= 0 的最高点。
        wi = 2 * i - n 
        for j in range(n + 1):
            wj = 2 * j - n
            
            # 这里的条件 `if wi < 0 and wj > 0:` 是关键。
            # 它寻找的是连接一个 wi < 0 的点 (i, p_i) 和一个 wj > 0 的点 (j, p_j) 的线段。
            # 这两个点分别对应于平均 a_k 小于 n/2 和平均 a_k 大于 n/2 的情况。
            # 如果 w_i 和 w_j 都小于等于 0，那么它们之间的线段也完全在 w <= 0 的区域。
            # 如果 w_i 和 w_j 都大于等于 0，那么它们之间的线段也完全在 w >= 0 的区域。
            # 只有当一个点在 w < 0 区域，另一个点在 w > 0 区域时，它们之间的线段才可能穿过 w = 0 这条线。
            # w = 0 对应于 a_k = n/2。
            # 这段代码尝试找到穿过 w = 0 (即 a_k = n/2) 的线段中，在 w = 0 处的最高点。
            if wi < 0 and wj > 0: 
                # 计算这条线段在 w = 0 处的纵坐标（即概率）。
                # 这实际上是在计算连接 (wi, nums[i]) 和 (wj, nums[j]) 的直线上，
                # 当横坐标为 0 时的纵坐标。
                # 通过相似三角形或者直线方程 y - y1 = ((y2 - y1) / (x2 - x1)) * (x - x1) 推导而来：
                # 设点为 (wi, pi) 和 (wj, pj)。我们要求当 x=0 时的 y 值。
                # y = pi + (pj - pi) / (wj - wi) * (0 - wi)
                # y = pi - wi * (pj - pi) / (wj - wi)
                # y = (pi * (wj - wi) - wi * (pj - pi)) / (wj - wi)
                # y = (pi * wj - pi * wi - wi * pj + wi * pi) / (wj - wi)
                # y = (pi * wj - wi * pj) / (wj - wi)
                ans = fmax(ans, (wj * nums[i] - wi * nums[j]) / (wj - wi))
    
    print(ans)
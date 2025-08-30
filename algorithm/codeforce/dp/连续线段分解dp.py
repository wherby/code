# https://codeforces.com/problemset/problem/201/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0828/solution/cf201c.md
# 这里过桥的路径就是一个连续的轨迹，其中一部分是来回的折线，另一部分是单向线段
# 而任意点的左右两边分别放单向线段和折线可以涵盖所有的case
# 对于DP而言，从左到右分析的时候，left0[i] 表示已经在i点，并且方向是单向向右移动，
#                            left1[i] 表示已经在i点，左边所有路径是折线，所以可以认为方向任意。
# ，如果左边是折线，则需要左边的连续区域都大于1， 这里不考虑奇偶性，因为大于1，在取折线的时候都取偶数值
# left0[i + 1] = fmax(left0[i] + nums[i] - (nums[i] + 1) % 2, left1[i] + nums[i]) 这里如果左边都是单向的： left0[i] + nums[i] - (nums[i] + 1) % 2 这里i，i+1 则只能取奇数，
#                                                                                 left1[i] + nums[i] ： 这一项，则表面，左边是折线，则要满足到i+1的时候，终点在i+1方向向右，nums[i] 可以都取
#                                                                                                       因为num[i+1]是奇数的时候，则可以i出发往左然后折线回来到达i+1， 如果num[i]是偶数，则可以从i+1出发往左，折线回来，在i+1的运动方向仍然是往右
# 对于右边同理。
#                   


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    left0 = [0] * n
    left1 = [0] * n
    
    for i in range(n - 1):
        if nums[i] > 1:
            left1[i + 1] = left1[i] + nums[i] // 2 * 2
        left0[i + 1] = fmax(left0[i] + nums[i] - (nums[i] + 1) % 2, left1[i] + nums[i])
    
    right0 = [0] * n
    right1 = [0] * n
    
    for i in range(n - 2, -1, -1):
        if nums[i] > 1:
            right1[i] = right1[i + 1] + nums[i] // 2 * 2
        right0[i] = fmax(right0[i + 1] + nums[i] - (nums[i] + 1) % 2, right1[i + 1] + nums[i])
    
    print(fmax(max(left0[i] + right1[i] for i in range(n)),
            max(left1[i] + right0[i] for i in range(n))))
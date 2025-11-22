# https://codeforces.com/gym/104536/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1120/solution/cf104536e.md
# LIS 变形技巧，如果分别计算nums1,nums2影响的DP,则可能需要线段树维护，如果直接用LIS 维护的话，先后插入会影响，使得同一位置使用两次
# 为了避免这个情况，把两个位置合并的时候，把大的放在前面则不会出现小的数字插入栈的时候使得栈变化，再插入大数的时候使用到了前一个数造成的影响
# 倒序遍历技巧


import init_setting
from lib.cflibs import *
from lib.lengthOfLIS import *
def main(): 
    n = II()
    nums1 = LII()
    nums2 = LII()
    
    vals = []
    
    for i in range(n):
        if nums1[i] > nums2[i]:
            vals.append(nums1[i])
            vals.append(nums2[i])
        else:
            vals.append(nums2[i])
            vals.append(nums1[i])
    
    print(lengthOfLIS(vals))

main()
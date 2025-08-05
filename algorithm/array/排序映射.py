# https://codeforces.com/problemset/problem/67/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0804/solution/cf67d.md
# 排列映射
#  pos1,pos2 存储 nums1,nums2数字x在对应数组nums1,nuns2中的索引
# ar[pos1[i]] = -pos2[i] 表示nums1中数字为i的值的索引位置，在nums2中数字为i的索引值的反值
# 换句话说，ar里存的是 i 在nums1 中的位置的索引地址上存了 i在nums2中索引的位置
# 
# nums1*pos1 = nums2*pos2
# 

import init_setting
from codeforce.lib.cflibs import *
from codeforce.lib.lengthOfLIS import *
def main():
    n = II()
    nums1 = LGMI()
    nums2 = LGMI()
    
    pos1 = [0] * n
    pos2 = [0] * n
    
    for i in range(n):
        pos1[nums1[i]] = i
        pos2[nums2[i]] = i
    
    ar = [0] * n
    
    for i in range(n):
        ar[pos1[i]] = -pos2[i]
    
    #print(ar,pos1,pos2)
    print(lengthOfLIS(ar))
    for i in range(n):
        print(nums1[pos1[i]],nums2[pos2[i]])

main()

# input:
# 5
# 1 4 5 2 3
# 3 4 2 1 5
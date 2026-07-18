# https://codeforces.com/gym/104182/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0919/solution/cf104182c.md
# 因为有 n*(n+1)//2个子数组，所以加上原数组的原始排序，所以有  1 + n * (n + 1) // 2
# 最值stack 的去重方式，双向去重之后，再加上重合部分
# 
    # stk = [-1]
    # for i in range(n):
    #     while stk[-1] != -1 and nums[i] >= nums[stk[-1]]:
    #         stk.pop()
    #     ans -= i - stk[-1]
    #     stk.append(i)
# 当前值在stack[-1]到当前为最大，所以前 i - stk[-1] 个subArray以当前值为右端点的子数组是重复的
    # stk = [n]
    # for i in range(n - 1, -1, -1):
    #     while stk[-1] != n and nums[i] <= nums[stk[-1]]:
    #         stk.pop()
    #     ans -= stk[-1] - i
    #     stk.append(i)
#  stk[-1] - i 个subarray以当前值为左端点的子数组是重复的

    # for i in range(n - 1, -1, -1):
    #     while stk1[-1] != n and nums[i] > nums[stk1[-1]]:
    #         stk1.pop()
        
    #     while stk2[-1] != n and nums[i] <= nums[stk2[-1]]:
    #         stk2.pop()
        
    #     l, r = 0, len(stk1) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if stk1[mid] >= stk2[-1]: l = mid + 1
    #         else: r = mid - 1
        
    #     ans += len(stk1) - l + 1
        
    #     stk1.append(i)
    #     stk2.append(i)
# stk1 是越来越小的单调数组，stk2表示越来越大的数组，
# stk1 (单调递减栈)：这个栈存储的索引 j，满足 nums[j] > nums[i]。它帮助我们找到以 nums[i] 为右端点，且所有元素都比 nums[i] 大的子数组。
# stk2 (单调递增栈)：这个栈存储的索引 k，满足 nums[k] <= nums[i]。它帮助我们找到以 nums[i] 为右端点，且所有元素都比 nums[i] 小或相等的子数组。
   #     while l <= r:
    #         mid = (l + r) // 2
    #         if stk1[mid] >= stk2[-1]: l = mid + 1
    #         else: r = mid - 1
# 如果端点在 stk2[-1]或者 右边，则以i点开始的所有排序都是新的，因为有 stk2[-1]这个点的引入
# 所以需要再这个点左边的所有比nums[i]大的“顶点” 递增数量，就是stk1中小于stk2[-1] 的数目， 为什么是“顶点递增” 如果有顶点，又小了一点，这个点不会引起重复，同时在stk1中被pop出去了
# 所以stk1中记录的点是valid点，同时也需要stk[-1]作为标记
# 所以二分选出的点满足 num[i]是最小的点， nums[j]是最大的点 满足 nums[i] <=min(nums[i+1:j-1]) and nums[j]>=max(nums[i+1:j-1])
# nums[i] <=min(nums[i+1:j-1]) 用stk2[-1] 决定，   nums[j]>=max(nums[i+1:j-1]) 由 skt1决定，两者需要求约束的交点，则二分答案


## 第一次循环只要 nums[i] >= nums[stk[-1]] 就表示当前值比栈内最小值大，则栈内的这个值在以后的排列中有或者没有的时候排列出的结果是一致的，所以可以pop掉，得到可以影响排序顺序的第一个值
## 同理从右到左，把右边又或者没有排列都一样的pop掉，
## 然后这样左右去除的情况有相交的部分，这时需要把重合的部分加回去 ： 
## 其实应该这样理解，stk2[-1]记录的是比当前值小的右向INDEX的最小值，这时这个INDEX左边的所有INDEX都满足当前值是最小值，这时就需要在这个区间内找到有多少个index可以作为最大值，这就是同时满足边界是最大最小值的个数了 
##  algorithm/codeforce/技巧/docs/双向Stack计算重合数量.md

import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    ans = 1 + n * (n + 1) // 2
    
    stk = [-1]
    for i in range(n):
        while stk[-1] != -1 and nums[i] >= nums[stk[-1]]:
            stk.pop()
        ans -= i - stk[-1]
        stk.append(i)
    
    stk = [n]
    for i in range(n - 1, -1, -1):
        while stk[-1] != n and nums[i] <= nums[stk[-1]]:
            stk.pop()
        ans -= stk[-1] - i
        stk.append(i)
    
    stk1 = [n]
    stk2 = [n]
    
    for i in range(n - 1, -1, -1):
        while stk1[-1] != n and nums[i] > nums[stk1[-1]]:
            stk1.pop()
        
        while stk2[-1] != n and nums[i] <= nums[stk2[-1]]:
            stk2.pop()
        
        l, r = 0, len(stk1) - 1
        while l <= r:
            mid = (l + r) // 2
            if stk1[mid] >= stk2[-1]: l = mid + 1
            else: r = mid - 1
        
        ans += len(stk1) - l + 1
        
        stk1.append(i)
        stk2.append(i)
    
    print(ans)
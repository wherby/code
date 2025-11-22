# https://leetcode.com/contest/weekly-contest-476/problems/count-stable-subarrays/
# 处理不完整段的前缀和，需要把 l，r 左边最右完整段的index 求出，这样求前缀和就只有1种情况  如果向先求中间的完整段，则会有3种情况： 中间有完整的段， 中间没有完整段， 有负的段 ，
# 先处理左边的时候需要ks<ke就是左边末尾是完整的， 处理右边的时候， start_final = max(l, s_prime) 这里确定了左右端点都在同一段的情况
# 也可以用莫队方式会超时 /Users/tao/software/code/algorithm/技巧/处理不完整段的前缀和/t4 copy.py
# 如果取中间完整线段的选择可以更简单

from typing import List, Tuple, Optional


from bisect import bisect_right,insort_left,bisect_left

from itertools import pairwise
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n= len(nums)
        ls = [-1]
        for i in range(n):
            if i >0 and nums[i]< nums[i-1]:
                ls.append(i-1)
        ls.append(n-1)
        pls = [0]
        for a,b in pairwise(ls):
            pls.append(pls[-1] + (b-a) *(b-a+1)//2)
        ret = []
        for l, r in queries:
            k_s = bisect_left(ls, l) - 1
            k_e = bisect_left(ls, r) - 1
            cnt = pls[k_e] - pls[k_s]
            if k_s < k_e and ls[k_s] < l:
                s = ls[k_s] + 1
                e = ls[k_s+1]
                le = l - s 
                
                if le > 0:
                    term1 = e - s + 1        
                    term_last = e - (l - 1) + 1  
                    excluded_sum = (term1 + term_last) * le // 2
                    cnt -= excluded_sum
            
            if k_e + 1 < len(ls): 
                s_prime = ls[k_e] + 1
                
                if s_prime <= r: 
                    start_final = max(l, s_prime)
                    end_final = r

                    length_final = end_final - start_final + 1

                    if length_final > 0:
                        cnt += length_final * (length_final + 1) // 2
            ret.append(cnt)
        return ret




from input import nums,queries
#re =Solution().countStableSubarrays(nums = [3,1,2], queries = [[0,1],[1,2],[0,2]])
re =Solution().countStableSubarrays(nums , queries)
print(re)
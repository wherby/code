# https://leetcode.cn/contest/weekly-contest-509/problems/palindromic-subarray-sum/description/
# algorithm/string/manachers/回文数组前缀和区间确定.py  对比起来，计算回文区间前后缀的，利用manchers 的结果，使用 (i+a)//2 (i-a)//2 刚好利用了奇偶性使得两个情况可以统一
from typing import List, Tuple, Optional




class Solution:
    def getSum(self, nums: List[int]) -> int:
        def manachers(A):
            
            Z = [0] * len(A)
            center = right =0
            for i in range(1,len(A)-1):
                if i < right:
                    Z[i] = min(right -i,Z[2*center -i]) # Z[2*center -i]是 i 关于center的对称点， 因为在[left, right]上对称，则 对称点的对称性是对称的
                while A[i + Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] +=1
                if i + Z[i] > right:
                    center,right = i , i+ Z[i]
            return Z[2:-2:1]
        ls = ["@","#"]
        for a in nums:
            ls.append(a)
            ls.append("#")
        ls.append("$")
        re = manachers(ls)
        pls=[0]
        for a in nums:
            pls.append(pls[-1]+a)
        mx = 0 
        for i,a in enumerate(re,2):
            if a > 0:
                st = (i-a)//2 
                ed = (i+a)//2 
                if st < ed:
                    mx = max(mx, pls[ed] - pls[st])
        return mx   
        

re =Solution().getSum( [1,1,2,3,2,1,5,6,6])
print(re)
# https://leetcode.cn/problems/count-special-subsequences/
# https://leetcode.cn/problems/count-special-subsequences/solutions/3033284/shi-zi-bian-xing-qian-hou-zhui-fen-jie-p-ts6n/
from typing import List, Tuple, Optional
from collections import Counter


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        c1= Counter()
        acc= 0
        for i in range(n-2):
            c2= Counter()
            if i >=4:
                b = nums[i-2]
                for j in range(i-3):
                    c1[nums[j]/b] +=1
                for j in range(i+2,n):
                    c2[nums[j]/nums[i]] +=1
                for k,v in c2.items():
                    acc +=v * c1[k]
        return acc
        
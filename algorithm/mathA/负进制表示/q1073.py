from typing import List, Tuple, Optional
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n1, n2 = len(arr1), len(arr2)

        # 1. 计算 arr1(base -2) + arr2(base -2) 的十进制表示
        num = 0

        for i in range(n1):
            num += arr1[i] * (-2) ** (n1 - 1 - i)
        for i in range(n2):
            num += arr2[i] * (-2) ** (n2 - 1 - i)

        # 2. 将十进制结果转化为负二进制(base -2)表示
        # 此处参考：[1017. 负二进制转换](https://leetcode.cn/problems/convert-to-base-2/)
        res = []

        while num:
            # r = 0 或 -1
            r = num % (-2)  
            res.append(-r)
            num = (num + r) // (-2)

        return res[::-1] if res else [0]
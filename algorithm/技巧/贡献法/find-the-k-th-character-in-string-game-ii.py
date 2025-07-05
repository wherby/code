# https://leetcode.cn/problems/find-the-k-th-character-in-string-game-ii/?envType=daily-question&envId=2025-07-04
# common include
# 操作1会 每一个k位置上的1都贡献了一次对应位置上的数字
from typing import List, Tuple, Optional

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        bls = bin(k-1)[2:][::-1]
        acc =0
        for i, a in enumerate(bls):
            if a =="1" and operations[i] ==1:
                acc +=1
        return chr(ord('a') + acc%26)

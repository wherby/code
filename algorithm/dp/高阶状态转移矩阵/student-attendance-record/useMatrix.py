# https://leetcode.cn/problems/student-attendance-record-ii/

import numpy as np


class Solution:
    def __init__(self):
        self.MOD = 1000000007

    def checkRecord(self, n):
        mat = np.array([[1, 1, 0, 1, 0, 0],
                        [1, 0, 1, 1, 0, 0],
                        [1, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 1, 0, 1],
                        [0, 0, 0, 1, 0, 0]])
        res = self.pow(mat, n)
        total = np.sum(res[0, :]) % self.MOD
        return int(total)

    def pow(self, mat, n):
        ret = np.eye(6, dtype=int)
        while n > 0:
            if n & 1:
                ret = self.multiply(ret, mat)
            n >>= 1
            mat = self.multiply(mat, mat)
        return ret

    def multiply(self, a, b):
        return np.dot(a, b) % self.MOD
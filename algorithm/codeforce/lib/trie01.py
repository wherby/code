# algorithm/codeforce/数论/数学/xor反向求值.py
# Tre01 可以查询当前数字和树里的数字最大和最小的xor结果
import math

class Trie01:
    def __init__(self, n):
        self.root = {'count': 0}
        self.bit_length = n.bit_length()

    def insert(self, value):
        node = self.root
        for i in range(self.bit_length - 1, -1, -1):
            node['count'] += 1
            bit = (value >> i) & 1
            if bit not in node:
                node[bit] = {'count': 0}
            node = node[bit]
        node['count'] += 1

    def remove(self, value):
        node = self.root
        for i in range(self.bit_length - 1, -1, -1):
            node['count'] -= 1
            bit = (value >> i) & 1
            node = node[bit]
        node['count'] -= 1
        
        # 注意：这里没有实现节点剪枝，如果需要，
        # 移除逻辑会更复杂，需要回溯。

    def find_max_xor(self, v):
        node = self.root
        ans = 0
        for i in range(self.bit_length - 1, -1, -1):
            bit = (v >> i) & 1
            opposite_bit = 1 - bit
            
            # 检查相反的路径是否存在且有有效节点
            if opposite_bit in node and node[opposite_bit]['count'] > 0:
                node = node[opposite_bit]
                ans |= (1 << i)
            else:
                # 否则走相同的路径
                node = node[bit]
        #print(ans)
        return ans

    def find_min_xor(self, v):
        node = self.root
        ans = 0
        for i in range(self.bit_length - 1, -1, -1):
            bit = (v >> i) & 1
            
            # 检查相同的路径是否存在且有有效节点
            if bit in node and node[bit]['count'] > 0:
                node = node[bit]
            else:
                # 否则走相反的路径
                opposite_bit = 1 - bit
                node = node[opposite_bit]
                ans |= (1 << i)
        return ans
    
    def count_lt_xor(self, v, x):
        """计算 Trie 中有多少个数字 val 满足 (val ^ v) < x"""
        node = self.root
        ans = 0
        for i in range(self.bit_length - 1, -1, -1):
            v_bit = (v >> i) & 1
            x_bit = (x >> i) & 1

            if x_bit == 1:
                # x 这一位是 1：
                # 1. 走相同的方向（异或结果在当前位为 0 < 1），
                # 该分支下的所有数字与 v 异或后都严格小于 x，全部累加！
                if v_bit in node and node[v_bit]['count'] > 0:
                    ans += node[v_bit]['count']

                # 2. 走相反的方向（异或结果在当前位为 1 == 1），继续往下比
                opposite_bit = 1 - v_bit
                if opposite_bit in node and node[opposite_bit]['count'] > 0:
                    node = node[opposite_bit]
                else:
                    break
            else:
                # x 这一位 Parent 是 0：
                # 异或结果必须为 0，只能走与 v_bit 相同的方向（对应异或 0 == 0）
                if v_bit in node and node[v_bit]['count'] > 0:
                    node = node[v_bit]
                else:
                    # 无法凑出 0，说明不可能产生 < x 的方案，直接 break
                    break

        # 循环结束说明 (val ^ v) == x。
        # 因为我们求的是严格小于 (< x)，所以【不累加】当前 node['count']
        return ans
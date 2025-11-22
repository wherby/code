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
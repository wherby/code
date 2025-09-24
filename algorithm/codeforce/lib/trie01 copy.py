
import math

class Trie01:
    def __init__(self, max_value, size):
        self.pt = 1
        self.bit = max_value.bit_length()
        # The C++ code uses __builtin_clzll to find the number of bits.
        # Python's int.bit_length() is the direct equivalent.
        
        total = size * self.bit + 1
        self.zero = [-1] * total
        self.one = [-1] * total
        self.cnt = [0] * total

    def insert(self, value):
        node = 0
        for i in range(self.bit - 1, -1, -1):
            self.cnt[node] += 1
            if (value >> i) & 1:
                if self.one[node] == -1:
                    self.one[node] = self.pt
                    self.pt += 1
                node = self.one[node]
            else:
                if self.zero[node] == -1:
                    self.zero[node] = self.pt
                    self.pt += 1
                node = self.zero[node]
        self.cnt[node] += 1

    def remove(self, value):
        node = 0
        for i in range(self.bit - 1, -1, -1):
            self.cnt[node] -= 1
            node = self.one[node] if (value >> i) & 1 else self.zero[node]
        self.cnt[node] -= 1

    def find_max_xor(self, v):
        node = 0
        ans = 0
        for i in range(self.bit - 1, -1, -1):
            if (v >> i) & 1:
                if self.zero[node] != -1 and self.cnt[self.zero[node]] > 0:
                    node = self.zero[node]
                    ans |= (1 << i)
                else:
                    node = self.one[node]
            else:
                if self.one[node] != -1 and self.cnt[self.one[node]] > 0:
                    node = self.one[node]
                    ans |= (1 << i)
                else:
                    node = self.zero[node]
        return ans

    def find_min_xor(self, v):
        node = 0
        ans = 0
        for i in range(self.bit - 1, -1, -1):
            if (v >> i) & 1:
                if self.one[node] != -1 and self.cnt[self.one[node]] > 0:
                    node = self.one[node]
                else:
                    node = self.zero[node]
                    ans |= (1 << i)
            else:
                if self.zero[node] != -1 and self.cnt[self.zero[node]] > 0:
                    node = self.zero[node]
                else:
                    node = self.one[node]
                    ans |= (1 << i)
        return ans

    def count_low_xor(self, num, x):
        if x >= (1 << self.bit):
            return self.cnt[0]
        
        node = 0
        ans = 0
        for i in range(self.bit - 1, -1, -1):
            if (x >> i) & 1:
                if (num >> i) & 1:
                    if self.one[node] != -1:
                        ans += self.cnt[self.one[node]]
                    if self.zero[node] != -1:
                        node = self.zero[node]
                    else:
                        break
                else:
                    if self.zero[node] != -1:
                        ans += self.cnt[self.zero[node]]
                    if self.one[node] != -1:
                        node = self.one[node]
                    else:
                        break
            else:
                if (num >> i) & 1:
                    if self.one[node] != -1:
                        node = self.one[node]
                    else:
                        break
                else:
                    if self.zero[node] != -1:
                        node = self.zero[node]
                    else:
                        break
        return ans
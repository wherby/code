# https://codeforces.com/gym/102788/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0130/solution/cf102788k.md
# 题目中给出了 n 个三进制字符串，从A移动到B的过程是汉诺塔的过程，
# 每个字符串表示一个汉诺塔的状态，
# 从后到前，遍历最高位， 当该位到target的时候，说明完成了一次从Source到target的移动，该位置一，其余各位反转车是从tmp到target的过程
# 若该位没有到target，则该位置为0，其余各位是在从sourec到tmp的过程,target和tmp交换



import init_setting
from cflibs import *
def main(): 
    n, m = MII()
    bin_2s = []
    
    for i in range(m):
        s = I()
        source, tmp, target = 'A', 'C', 'B'
        
        bin_2 = []
        
        for c in reversed(s):
            if c == target:
                bin_2.append(1)
                source, tmp = tmp, source
            else:
                bin_2.append(0)
                tmp, target = target, tmp
        
        bin_2s.append(bin_2)
    
    print(bin_2s.index(max(bin_2s)) + 1)
# https://codeforces.com/gym/104013/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0214/solution/cf104013c.md
# 双向排序，冒泡法，和逆冒泡，冒泡法能让最大的元素冒泡到末尾，逆冒泡能让最小的元素冒泡到开头，交替进行 n-1 轮就能完成排序
# 每次两个方法都做一遍，可以对抗一次干扰交换



import init_setting
from cflibs import *
def main(): 
    def swap(i, j):
        print(i, j, flush=True)
        if I()[0] == 'W': exit()
    
    n = II()
    
    for _ in range(n):
        for i in range(1, n):
            swap(i, i + 1)
        
        for i in range(n, 2, -1):
            swap(i - 1, i)
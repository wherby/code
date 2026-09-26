# https://codeforces.com/gym/106097/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0902/solution/cf106097f.md
# 这里所有的图像是两段的凹点，如果用二进制倍增的话不容易求出两个点
# 用二分先求一个凹点，然后再次在两个区域二分求
# 把每个位置的符号写出来，整个序列呈现出 >>...>=<<..<>>...>=<<...< 的形式
# 这里有一个特性,中间序列的关系是对称的，所以用 fmax(search(1, find1 - 1), search(find1 + 1, n)) 二分的第一个点形成的区域 一定有个区域是符合凹点图形的
 

import init_setting
from cflibs import *
def main():
    def query(x):
        print(x, flush=True)
        return I()
    
    def answer(x1, x2):
        print('!', x1, x2)
    
    def search(l, r):
        while l <= r:
            mid = (l + r) // 2
            res = query(mid)
            
            if res == '=': return mid
            
            if res == '<': r = mid - 1
            else: l = mid + 1
        
        return -1
    
    n = II()
    find1 = search(1, n)
    find2 = fmax(search(1, find1 - 1), search(find1 + 1, n))
    
    if find1 > find2: find1, find2 = find2, find1
    answer(find1, find2)
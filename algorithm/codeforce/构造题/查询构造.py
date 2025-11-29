# https://codeforces.com/gym/106197/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1127/solution/cf106197c.md
# 如果 pos 的值是1 ，则 gcd(nums[pos], nums[i]) 返回的index 就是pos ,这时就可以知道pos 的值不是1了  algorithm/codeforce/构造题/查询构造验证/test.py
# 同理，在剩余的index里查询，期望找到和其他都不互质的数字，如果当前index 和另一个index 的gcd 不是1的index,则说明这两个index不互质，则二者都可以舍去，返回值的index 更“接近”于质数，把返回值当做candidate测试，
# 这样循环一遍，则candidate 一定是和所有被测试值都更接近质数的，这就是质数了。
# 如果 二者gcd是1的 index ,则 测试对象可能是质数，则测试值被加入下一次循环被测试

import init_setting

from cflibs import *
def main(): 
    def query(x, y):
        print('?', x, y, flush=True)
        return II()
    
    def answer(idxs):
        print('!', len(idxs), *(idx for idx in idxs))
    
    n = II()
    pos1 = 1
    
    for i in range(2, n + 1):
        if query(pos1, i) != pos1:
            pos1 = i
    
    cur = [i for i in range(1, n + 1) if i != pos1]
    ans = []
    
    while cur:
        ncur = []
        prime_val = cur[0]
    
        for i in range(1, len(cur)):
            v = query(prime_val, cur[i])
            
            if v == pos1: ncur.append(cur[i])
            else: prime_val = v
        
        cur = ncur
        ans.append(prime_val)
    
    answer(ans)
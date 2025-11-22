# https://codeforces.com/gym/104936/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1120/solution/cf104936e.md
# 把相等的SubArray 数量转换为 小于等于的数量之差， 为什么不能转换为大于等于只差？ 因为我们要维护一个双指针系统，插入数字的时候，Xor的总值是越来越小，不是越来越大
# 用Trie01树计算数字与树上的数字最大或者最小的Xor结果

import init_setting
from cflibs import *
from lib.trie01 import Trie01
def main(): 
    n, k = MII()
    nums = LII()
    
    def solve(val):
        ans = 0
        
        trie = Trie01( (1 << 30) - 1)
        l = r = 0
        while l < n:
            while r < n:
                if l == r:
                    trie.insert(nums[l])
                else:
                    if trie.find_min_xor(nums[r]) >= val:
                        trie.insert(nums[r])
                    else: break
                r += 1
            
            ans += r - l
            
            trie.remove(nums[l])
            l += 1
        
        return ans
    
    print(solve(k) - solve(k + 1))

main()
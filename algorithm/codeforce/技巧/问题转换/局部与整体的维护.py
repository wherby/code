# https://codeforces.com/gym/106671/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0829/solution/cf106671c.md
# 在倍增操作的情况下，如果当前数组的长度超过可以被删除的操作数的话，则操作的队列和不用倍增的队列一致“因为倍增中间的数字永远不能被操作到”
# 所以就可以想象当前队列是一个不定长度的“Ring buffer”,增加和删除就只能在边界操作，


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    mod = 998244353
    
    cur = sum(nums) % mod
    
    M = 10 ** 6 * 2
    que_array = [0] * M
    
    l = 5 * 10 ** 5
    r = l + n
    
    for i in range(n):
        que_array[l + i] = nums[i]
    
    flg = True
    
    q = II()
    outs = []
    
    for _ in range(q):
        query = LII()
        
        if query[0] == 1:
            if flg:
                que_array[r] = query[1]
                r += 1
            else:
                l -= 1
                que_array[l] = query[1]
            
            cur = (cur + query[1]) % mod
        
        elif query[0] == 2:
            if flg:
                r -= 1
                cur -= que_array[r]
            else:
                cur -= que_array[l]
                l += 1
            
            cur %= mod
        
        elif query[0] == 3:
            flg = not flg
        
        elif query[0] == 4:
            cur = cur * 2 % mod
            
            if r - l < q:
                for i in range(r - l):
                    que_array[r + i] = que_array[l + i]
                
                r += r - l
        
        else:
            outs.append(cur)
    
    print('\n'.join(map(str, outs)))
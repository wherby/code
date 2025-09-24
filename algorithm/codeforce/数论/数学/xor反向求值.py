# https://codeforces.com/gym/104777/problem/N
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0923/solution/cf104777n.md
# 这里已知n-1个数字不相同，则pairwise xor 后的结果是n-2个，因为不相同，则0 一定不在xor结果里，所以需要先加上0
# 因为trie里面已经有n-1个不同向量，且0包含在里面，要使得所有向量是 0 到 n-1的满排列，则最大的xor值不应该大于n-1？
# 因为 ans[0] = [i] ans[1] = [i] xor nums[0] ,ans2 = ([i] xor nums[0]) xor (nums[0] xor nums[1]) = [i] xor nums[1] 以此类推
# [i] xor nums[j] 的最大值是 n-1 
# 由于要使得所有xor结果的最大值为n-1,才能满足新数列的结果是全排列？

import init_setting
from cflibs import *
from lib.trie01 import Trie01
def main():
    n = II()
    nums = LII()
    
    trie = Trie01(n*2)
    
    for i in range(1, n - 1):
        nums[i] ^= nums[i - 1]
    trie.insert(0)
    for x in nums:
        trie.insert(x)
    
    for i in range(n):
        if trie.find_max_xor(i) == n - 1:
            ans = [i] + [i ^ x for x in nums]
            print(' '.join(map(str, ans)))
            break

main()
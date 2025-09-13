# https://codeforces.com/problemset/problem/901/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0905/solution/cf901a.md
# 这里是需要标记子节点的父节点， chosen_node[depth[i]] = i 在每一层有多个数字的时候，会重复写入，但是会保留当前层的最大的节点序号


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    for h in range(n):
        if nums[h] > 1 and nums[h + 1] > 1:
            print('ambiguous')
            
            total = sum(nums)
            
            depth = [0] * total
            chosen_node = [0] * (n + 1)
            
            pt = 0
            
            for i in range(total):
                while nums[pt] == 0: pt += 1
                depth[i] = pt
                nums[pt] -= 1
                chosen_node[depth[i]] = i
            
            ans = [0] * total
    
            for i in range(1, total):
                ans[i] = chosen_node[depth[i] - 1] + 1
            
            print(' '.join(map(str, ans)))
            
            for i in range(1, total):
                if depth[i] == h + 1:
                    ans[i] = chosen_node[depth[i] - 1]
                    break
            
            print(' '.join(map(str, ans)))
            
            exit()
    
    print('perfect')
# https://codeforces.com/gym/104974/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0618/solution/cf104974m.md
# 虽然是求树上的点去掉之后的联通区域的数量， 但是这里是把每一条边单独计算, 
# 如果去掉的值和两个边上的点都不能整除，则无关，与其中一个整除，则增加了1个联通区域
# 然而去除一个点的情况很难计算，这里其实使用的差分标记， notes[math.gcd(nums[u], nums[v])] -= 1 ，notes[nums[v]] += 1 ，notes[nums[u]] += 1，这里是看每个值能作为父亲节点的个数，因为每个点在树上只能当1次儿子，所以
# for x in nums:
#        notes[x] -= 1  这时剩下的就是该值作为父亲的个数，根节点要特殊处理
# 这里不仅仅是1倍的简单代数变化，而是记录了每个值作为父亲
# 如果 k = m* math.gcd(nums[u], nums[v] m>1的时候，才有可能刚好只是一个点的倍数
# 这时谁是父亲谁是儿子在这里不关键？ 假设去掉的是叶子,这时发现，叶子这个值作为父节点的积累是0，则区域不增加
#   for x in nums:
#        notes[x] -= 1
# algorithm/codeforce/docs/图论树上GCD差分标记.md


import init_setting
from cflibs import *
def main():
    n, k = MII()
    nums = LII()
    
    M = 10 ** 6 + 5
    
    notes = [0] * M
    
    for _ in range(n - 1):
        u, v = GMI()
        notes[nums[u]] += 1
        notes[nums[v]] += 1
        notes[math.gcd(nums[u], nums[v])] -= 1
    
    for x in nums:
        notes[x] -= 1
    
    notes[nums[0]] += 1
    
    ans = []
    
    for i in range(1, k + 1):
        res = 0
        for j in range(i, M, i):
            res += notes[j]
        if nums[0] % i:
            res += 1
        ans.append(res)
    
    print(' '.join(map(str, ans)))
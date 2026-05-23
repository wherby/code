# https://codeforces.com/gym/106414/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0505/solution/cf106414f.md
# 需要找到三个数字和 m<= x+y+z <=2*m 的组合
# 可以根据排序得到两部分选择区域， [1,m),[m,2m) 
# 满足条件的必然是是 第一个第二区域的数字 和最小的两个数字，
# 或者第一区域的最大最小的三个数字的组合
# 这样就避免了三指针等的计算




import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        nums = LII()
        
        order = sorted(range(n), key=lambda x: nums[x])
        
        ans = []
        bound = n
        
        for i in range(2, n):
            if nums[order[i]] >= m:
                if nums[order[0]] + nums[order[1]] + nums[order[i]] <= 2 * m:
                    ans = [order[0], order[1], order[i]]
                bound = i
                break
        
        if not ans and bound >= 3:
            for i in range(4):
                tmp = []
                for j in range(i):
                    tmp.append(order[j])
                for j in range(3 - i):
                    tmp.append(order[bound - 1 - j])
                
                total = 0
                for x in tmp:
                    total += nums[x]
                
                if m <= total <= 2 * m:
                    ans = tmp
                    break
        
        if ans: outs.append(' '.join(str(x + 1) for x in ans))
        else: outs.append('-1')
    
    print('\n'.join(map(str, outs)))
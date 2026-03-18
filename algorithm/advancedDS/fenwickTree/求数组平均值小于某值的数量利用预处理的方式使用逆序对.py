# https://codeforces.com/gym/106421/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0313/solution/cf106421g.md
# 坐标平移再处理？
# 把问题变成连续数组数组平均值的计算 N(平均值 <=b) - N(平均值 <a) 的个数， 等于的时候，我们需要缩放增加最小delta，1/n, 缩放的时候增加n倍，
#  algorithm/codeforce/docs/连续数组平均值的预处理.md  《=为什么要写成   (nums[i] * n - (b * n + 1)) 的方式
# 然后使用逆序对的方式求解
# algorithm/codeforce/docs/连续数组平均值的预处理.md



import init_setting
from cflibs import *
from lib.fenwicktreeReversedPair import reversePairs
def main(): 
    n, a, b = MII()
    nums = LII()
    
    ans = 0
    
    acc = [0] * (n + 1)
    
    for i in range(n):
        acc[i + 1] = acc[i] + (nums[i] * n - (b * n + 1))
    
    ans += reversePairs(acc)
    
    for i in range(n):
        acc[i + 1] = acc[i] + (nums[i] * n - a * n)
    
    ans -= reversePairs(acc)
    
    print(ans)

if __name__ == '__main__': 
    main()
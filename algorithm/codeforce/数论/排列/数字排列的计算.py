# https://codeforces.com/gym/106296/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0110/solution/cf106296f.md
# A= 1 1 0 1 0 1 0 表示了什么意思？ 就是第1,2,4,6 位上是奇数，其余的是偶数？
# 简单直接地说：不是的，你的理解刚好反了。
# 这个 A 数组不是在描述“第几位”，而是在描述**“数字本身”**。
# 在题目中，数字 1,2,3,4,5,6,7 是我们要填入排列的“素材”。A 数组是这些素材的说明书：
# A1=1：数字 1 必须放在奇数位
# A2=1：数字 2 必须放在奇数位。
# A3=0：数字 3 必须放在偶数位
# A4=1：数字 4 必须放在奇数位。
# A5=0：数字 5 必须放在偶数位。
# A6=1：数字 6 必须放在奇数位。
# A7=0：数字 7 必须放在偶数位。
# algorithm/codeforce/数论/排列/排列数字表示/index.md
# 理解了上面的 A 的意义，则遍历A， 因为奇数位上的数字小于偶数位的数字，所以先从左到右遍历，如果是奇数，则表示当前对的数字已经插入到奇数位了，遇到0， 则可以在当前插入的奇数的位置的右边放置该数字，消耗一个插入位
# 
# 同理从右到左遍历的时候，这时的数字是从大到小的，这时候如果是0，则表示该数字可以作为偶数插口放置，这时处理的是奇数插入的时候的个数，遇到奇数的时候，因为已经积累了偶数的插口，则消耗一个插口插入该奇数到偶数插口的左边

# 从左到右，从右到左，这时分别计算了两种类型插口在插入的排列数量，所以是可以乘积在一起的




import init_setting
from cflibs import *
def main(): 
    n = II()
    nums = LII()
    
    mod = 998244353
    
    ans = 1
    cur = 0
    
    for i in range(n):
        if nums[i]: cur += 1
        else:
            ans = ans * cur % mod
            cur -= 1
    
    cur = 0
    for i in range(n - 1, n % 2 - 1, -1):
        if nums[i]:
            ans = ans * cur % mod
            cur -= 1
        else:
            cur += 1
    
    print(ans)
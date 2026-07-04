

from functools import cache
mod = 10**9+7

def count_with_template(m):
    # 将 m 转换为二进制字符串，例如 m = 12 -> '1100'
    s = bin(m)[2:]
    n = len(s)

    @cache
    def f(i, is_limit, cnt):
        """
        i: 当前处理到二进制字符串的第 i 位（从高到低）
        is_limit: 是否受到 m 的限制（贴边状态）
        cnt: 从最高位到当前位置，已经填了多少个 `1`
        """
        # 边界条件：当所有位都填完时
        if i == n:
            # 走到这里意味着得到了一个合法的数字，我们返回它已经包含的 1 的个数
            # 为了后面方便统计，我们这里直接返回一个计数数组，或者在外部枚举 i
            return [1 if k == cnt else 0 for k in range(n + 1)]
        
        # 初始化当前状态下，各种“1的个数”的方案数数组
        # 比如 res[3] = 5 表示此分支后面能进化出 5 个“总共含有 3 个 1 的数字”
        res = [0] * (n + 1)
        
        # 根据当前是否受限，决定这一位最大能填到几（二进制只能填 0 或 1）
        up = int(s[i]) if is_limit else 1
        
        # 枚举当前位填 d (0 或 1)
        for d in range(0, up + 1):
            # 递归调用下一位
            next_res = f(i + 1, is_limit and (d == up), cnt + d)
            
            # 将下一位返回的所有可能结果累加到当前层
            for k in range(n + 1):
                res[k] = (res[k] + next_res[k]) % mod
                
        return res

    # 最终返回的 ans_array[k] 就表示 0 ~ m 中，二进制含有 k 个 1 的数字有多少个
    return f(0, True, cnt=0)

# 递推形式

def countToM(m):
    m = m+1
    dp = [0]*60
    c = 0 
    
    for i in range(59,-1,-1):
        for j in range(58,-1,-1):
            dp[j+1] += dp[j]
        if m >>i &1 :
            dp[c] +=1
            c +=1
    return [a%mod for a in dp]

import random
A = 10**10 + random.randint(10,100000)
ls1 = countToM(A)
ls2 = count_with_template(A)
acc = 0 
print(ls1)
print(ls2)
for a,b in zip(ls1,ls2):
    if a ==b:
        acc +=1
    else:
        print("Not eqaul :",a,b)
print(acc,"is eqaul for ls1,ls2") 


from fractions import Fraction

def berlekamp_massey_exact(a):
    """
    精确分数版本的 Berlekamp-Massey 算法
    适用于整数数列，返回有理系数
    """
    n = len(a)
    if n == 0:
        return []
    
    coef = []        # 当前递推式系数（Fraction）
    pre_coef = []    # 上一次出错时的递推式
    tmp = []         # 临时存储
    
    pre_i = -1       # 上一次出错的位置
    pre_d = Fraction(0, 1)  # 上一次出错的差值
    
    for i in range(n):
        # 计算预测值与实际值的差值 d
        d = Fraction(a[i], 1)
        
        # 用当前递推式计算预测值
        for j in range(len(coef)):
            d -= coef[j] * a[i - 1 - j]
        
        # 预测正确，继续
        if d == 0:
            continue
        
        # 第一次出错：初始化递推式为 i+1 个 0
        if pre_i < 0:
            coef = [Fraction(0, 1)] * (i + 1)
            pre_i = i
            pre_d = d
            continue
        
        # 非第一次出错，修正递推式
        bias = i - pre_i
        
        # 可能需要扩展递推式的长度
        old_len = len(coef)
        new_len = bias + len(pre_coef)
        
        if new_len > old_len:
            tmp = coef[:]
            coef.extend([Fraction(0, 1)] * (new_len - old_len))
        
        # 计算修正系数 delta = d / pre_d
        delta = d / pre_d
        
        # 修正递推式
        if 0 <= bias - 1 < len(coef):
            coef[bias - 1] += delta
        
        for j in range(len(pre_coef)):
            idx = bias + j
            if idx < len(coef):
                coef[idx] -= delta * pre_coef[j]
        
        # 如果递推式长度增加了，更新 pre_coef
        if new_len > old_len:
            pre_coef = tmp[:]
            pre_i = i
            pre_d = d
    
    # 转换为整数系数（如果可能）
    result = []
    for c in coef:
        if c.denominator == 1:
            result.append(c.numerator)
        else:
            # 无法转换为整数，返回分数
            result.append(c)
    
    # 去除末尾的零
    while result and result[-1] == 0:
        result.pop()
    
    return result

if __name__ == '__main__':
    # https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/solutions/3869310/san-chong-fang-fa-ji-yi-hua-sou-suo-di-t-tell/?envType=daily-question&envId=2026-01-03
    arr = [12, 54, 246, 1122, 5118, 23346, 106494, 485778, 2215902]
    coef=berlekamp_massey_exact(arr)
    print(coef)

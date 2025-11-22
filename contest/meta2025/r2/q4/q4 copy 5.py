MOD = 998244353

def count_k_weak(L, R, K):
    """计算[L,R]中K-弱密码的数量"""
    
    def count_non_weak_up_to(limit):
        """计算[0,limit]中非K-弱的数字数量"""
        if limit < 0:
            return 0
            
        digits = list(map(int, str(limit)))
        n = len(digits)
        
        # 如果位数 >= K，根据鸽巢原理都是K-弱
        if n >= K:
            return count_all_non_weak_up_to_length(K - 1)
        
        # 使用旋转掩码DP
        return count_with_rotation_dp(digits, n)
    
    def count_with_rotation_dp(digits, n):
        """使用旋转掩码DP计算非K-弱数字"""
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dp(mask, tight, pos):
            """
            mask: 旋转后的位掩码，当前前缀和总是在bit 0
            tight: 是否受上界限制
            pos: 当前处理的位置
            """
            if pos == n:
                # 检查是否是一个有效的数字（至少1位）且所有前缀和不同
                # mask中bit 0总是被占用（当前前缀和），所以popcount应该=pos+1
                return 1 if bin(mask).count('1') == pos + 1 else 0
            
            res = 0
            upper = digits[pos] if tight else 9
            
            for dig in range(0, upper + 1):
                new_tight = tight and (dig == upper)
                
                # 新的前缀和 = (0 + dig) % K （因为当前前缀和在bit 0）
                new_sum = dig % K
                
                # 检查新的前缀和是否已经出现过
                if mask & (1 << new_sum):
                    continue
                
                # 旋转mask：新的当前前缀和移到bit 0
                # 1. 清除原来的bit 0（当前前缀和）
                # 2. 将其他位右移，为新的前缀和腾出位置
                # 3. 设置新的bit 0
                
                # 更简单的方法：重新构建mask
                # 保留除了bit 0以外的所有位
                old_bits = mask & (~1)
                # 将这些位右移1位（相当于除以2）
                rotated_mask = old_bits >> 1
                # 设置新的前缀和到bit 0
                new_mask = rotated_mask | (1 << new_sum)
                
                res += dp(new_mask, new_tight, pos + 1)
            
            return res % MOD
        
        # 初始状态：mask只有bit 0被设置（s0=0），tight=True，pos=0
        return dp(1, True, 0)
    
    def count_all_non_weak_up_to_length(max_len):
        """计算所有位数不超过max_len的非K-弱数字数量"""
        total = 0
        for length in range(1, min(max_len, K - 1) + 1):
            total = (total + count_fixed_length_non_weak(length)) % MOD
        return total
    
    def count_fixed_length_non_weak(length):
        """计算固定长度的非K-弱数字数量"""
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dfs(mask, pos):
            """
            mask: 旋转后的位掩码
            pos: 当前处理的位置
            """
            if pos == length:
                return 1 if bin(mask).count('1') == pos + 1 else 0
                
            res = 0
            start_digit = 1 if pos == 0 else 0
            
            for dig in range(start_digit, 10):
                new_sum = dig % K
                if mask & (1 << new_sum):
                    continue
                
                # 旋转mask
                old_bits = mask & (~1)
                rotated_mask = old_bits >> 1
                new_mask = rotated_mask | (1 << new_sum)
                
                res += dfs(new_mask, pos + 1)
            
            return res % MOD
        
        # 初始状态：mask只有bit 0被设置
        return dfs(1, 0)
    
    # 主逻辑
    total_numbers = (R - L + 1) % MOD
    non_weak_R = count_non_weak_up_to(R)
    non_weak_L_minus = count_non_weak_up_to(L - 1)
    non_weak_count = (non_weak_R - non_weak_L_minus) % MOD
    
    return (total_numbers - non_weak_count) % MOD

# 测试代码
def test():
    # 测试用例：29231是7-弱，512不是7-弱
    L, R, K = 1, 1000, 7
    result = count_k_weak(L, R, K)
    print(f"L={L}, R={R}, K={K}: {result}")
    
    # 测试K=25的情况
    L, R, K = 1, 10**60, 25
    result = count_k_weak(L, R, K)
    print(f"L={L}, R={R}, K={K}: {result}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        data = sys.stdin.read().split()
        if data:
            L, R, K = map(int, data[:3])
            print(count_k_weak(L, R, K))
    else:
        test()
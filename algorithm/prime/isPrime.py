#https://leetcode.cn/circle/discuss/ufi3Z8/view/uAhR8k/

# 

def isPrime(num):
    if num == 1: return False
    i = 2
    while i * i <= num:   # 可以先求prime list 加速
        if num % i == 0: return False
        i += 1
    return True


#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/ufi3Z8/view/uAhR8k/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

def is_prime(self, n: int) -> bool:
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n >= 2  # 1 不是质数

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/prime-in-diagonal/solutions/2216347/pan-duan-zhi-shu-by-endlesscheng-m6nt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
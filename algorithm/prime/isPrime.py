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
from math import sqrt

def get_prime_factor(num):
    # 质因数分解
    res = []
    for i in range(2, int(sqrt(num)) + 1):
        cnt = 0
        while num % i == 0:
            num //= i
            cnt += 1
        if cnt:
            res.append([i, cnt])
        if i > num:
            break
    if num != 1 or not res:
        res.append([num, 1])
    return res

print(get_prime_factor(124888000))

print(get_prime_factor(13917501265))
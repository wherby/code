# https://codeforces.com/gym/106179/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1110/solution/cf106179c.md
# 构造 Xor 的时候，需要考虑两数字不要有重合，和低位重合的情况使得  Xor和是倍数
# 
import math
def getAB(c):
    n = c.bit_length()+1
    return C <<(n),(C <<n) + c


def verify(A,B,C):
    S1 = (A^C) + (B^C)
    S2 = math.lcm(A,C) + math.lcm(B,C)
    return S1,S2

C =119
A,B = getAB(C)
print(verify(A,B,C))

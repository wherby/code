# https://leetcode.cn/contest/biweekly-contest-130/problems/find-products-of-elements-of-big-array/


## For 1 to n there are x of number of kth bit set 

def getKBit(n,k):
    return n//(1<<(k+1)) *(1<<k) + max(0, n %(1<<(k+1)) - (1<<k)+1)

print(getKBit(14,2))
print(getKBit(6,2)) 


def getKBitsArray(n):
    return [n//(1<<(k+1)) *(1<<k) + max(0, n %(1<<(k+1)) - (1<<k)+1) for k in range(50)]


## Get bit set nums of 1 to n :

def getBits(n):
    acc = 0
    for i in range(50):
        acc += n//(1<<(i+1)) *(1<<i) + max(0, n %(1<<(i+1)) - (1<<i)+1)
    return acc

# 算n 位2进数有多少个置位
# N(0) = 0
# N(i+1) = N(i)*2 +2^i
# N(n) = n*2^(n-1) 

print(getBits((1<<31)-1))
print(31*(2**30))
# https://leetcode.cn/contest/biweekly-contest-82/problems/minimum-sum-of-squared-difference/

from turtle import right


def arrayChangeWithK(ls,k):
    left,right = 0,10**11
    count =0
    while left < right:
        mid = (left+right)>>1
        sm = 0
        for a in ls:
            sm += max(0, a -mid )
        if sm >k:
            left = mid +1
        else:
            right = mid 
            count = k - sm 
    ret= []
    if left ==0:
        return [0]*len(ls)
    for a in ls:
        if a < left:
            ret.append(a)
        else:
            ret.append(left -min(1,max(0,count)))
            count -=1
    return ret


ls = [1,3,7,8,9]
print(arrayChangeWithK(ls,0))
print(arrayChangeWithK(ls,4))
print(arrayChangeWithK(ls,26))
print(arrayChangeWithK(ls,23))
print(arrayChangeWithK(ls,28))
print(arrayChangeWithK(ls,27))
print(arrayChangeWithK(ls,49))
    
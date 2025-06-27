
import random


def fx():
    ls = []
    for _ in range(10):
        ls.append(random.randint(1,10))

    print(ls)

    for i,a in enumerate(ls,1):
        sm = sum(ls) - a 
        k = (i-sm)%10 +1
        print(i,k, a)
fx()
# https://codeforces.com/problemset/problem/690/A3
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0621/solution/cf690a3.md
# 一个任意生成的【1，N】的序列，自己可以看到除了自己的其他人的数字，并且知道自己的排序，则可以得到另一个序列，满足有且仅有一个位置上的数字相等


def fx2():
    ls = []
    for _ in range(10):
        ls.append(random.randint(1,10))

    cnt = 0
    ls2 = []
    acc = 0 
    for i,a in enumerate(ls,1):
        sm = sum(ls) - a 
        k = (i-sm)%10 +1
        if k ==a :
            cnt +=1
        ls2.append(k)
        
    if cnt != 1:
        print(ls,ls2)
    #print(sum(abs(a-b) for a,b in zip(ls,ls2)))


for _ in range(10000):
    fx2()
print("done")

## 证明
# 假设 sum(ls) %N == X
#  (i-sm) = (i+ Ai - X ) %N  
#当 i ==X 的时候， 就是Ai 因为 i 是从 1 到N 必然只有1个值是 X， 则有且只有1个值相等

## From algorithm/kth
# 全排列有重复的情况

ls = [a]*a1 + [b]*b1 + [c]*c1

的全排列数量是
C(a1+b1+c1,a1) + C(b1+c1,b1) + C(c1,c1)

C(a1+b1+c1,b1) +C(a1+c1,a1) + C(c1,c1) == C(a1+b1+c1,a1) + C(a1+c1,a1) + C(c1,c1)

试填法： 
满足 a<b<c 


```python https://leetcode.cn/problems/smallest-palindromic-rearrangement-ii/solutions/3649533/shi-tian-fa-zu-he-shu-xue-pythonjavacgo-qlu6e/

def perm(sz: int) -> int:
    res = 1
    for c in ls:
        if c == 0:
            continue
        # 先从 sz 个里面选 c 个位置填当前字母
        res *= comb(sz, c)
        if res >= k:  # 太大了
            return k
        # 从剩余位置中选位置填下一个字母
        sz -= c
    return res
ret = []
ls = [a1,b1,c1]
m = a1+b1+c1
for i in range(m):
    for j,key in enumerate([a,b,c]):
        if ls[j] ==0:continue 
        ls[j] -=1 
        p = perm(m-i-1)
        if p >=k:
            ret[i] = key
            break
        k-=p
        ls[j] +=1
```

```python
# 构造回文串的左半部分
        left_s = [''] * m
        for i in range(m):
            for j in range(26):
                if cnt[j] == 0:
                    continue
                cnt[j] -= 1  # 假设填字母 j，看是否有足够的排列
                p = perm(m - i - 1)  # 剩余位置的排列个数
                if p >= k:  # 有足够的排列
                    left_s[i] = chr(ord('a') + j)
                    break
                k -= p  # k 太大，要填更大的字母
                cnt[j] += 1


#作者：灵茶山艾府
#链接：https://leetcode.cn/problems/smallest-palindromic-rearrangement-ii/solutions/3649533/shi-tian-fa-zu-he-shu-xue-pythonjavacgo-qlu6e/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

通过试填法得出:
C(a1+b1+c1,a1) + C(b1+c1,b1) + C(c1,c1) = P(a1+b1+c1-1,a1-1) +P(a1+b1+c1-1,b1-1) +P(a1+b1+c1-1,c1-1) ??

test 证明  algorithm/kth/test.py


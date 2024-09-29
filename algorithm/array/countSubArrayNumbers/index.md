



## 求subarray的数量 都用slidwindow， 比如求所有subarray 的 uniqueness
https://leetcode.cn/contest/weekly-contest-395/problems/find-the-median-of-the-uniqueness-array/

class Solution(object):
    def medianOfUniquenessArray(self, nums):
        n = len(nums)
        hf =  ((n+1) *n //2 )//2 +1

        def verify(mid):
            l =0 
            c = defaultdict(int)
            acc=0
            for i,a in enumerate(nums):
                c[a] += 1
                while len(c)>= mid:
                    c[nums[l]] -=1
                    if c[nums[l]] ==0:
                        del c[nums[l]]
                    l +=1
                acc += l
            return acc >= hf 
        l,r = 1, n 
        while l < r :
            mid = (l+r+1)>>1
            if verify(mid):
                l= mid
            else:
                r = mid-1
        return l 

## 求刚好有k个就等价于 求多余k - 多余k+1
N(K)= O(n>=k) - O(n>=(k+1))

https://leetcode.cn/contest/weekly-contest-417/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/

class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        def solve(w, k):
            c = Counter()
            j = 0
            z = 0
            for i in range(len(w)):
                if w[i] in 'aeiou':
                    c[w[i]] += 1
                else:
                    c['_'] += 1
                while c['a'] > 0 and c['e'] > 0 and c['i'] > 0 and c['o'] > 0 and c['u'] > 0 and c['_'] >= k:
                    if w[j] in 'aeiou':
                        c[w[j]] -= 1
                    else:
                        c['_'] -= 1
                    j += 1
                z += j
            return z
        return solve(w, k) - solve(w, k + 1)
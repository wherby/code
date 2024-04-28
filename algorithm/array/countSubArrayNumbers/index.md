



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
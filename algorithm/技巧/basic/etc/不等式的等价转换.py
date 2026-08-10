# https://leetcode.cn/problems/count-subarrays-with-even-odd-ratio-ii/
# https://leetcode.cn/problems/count-subarrays-with-even-odd-ratio-ii/solutions/4005429/deng-jie-zhuan-hua-qian-zhui-he-ni-xu-du-2ygw/
# 这里的比例不等式   等价与不同类型元素有不同值的求和
#  x/y <= a/b  => a*y - b*x >=0 
class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)
        self.bit= [0]*self.n
        for i in range(self.n):
            self.add(i,arr[i])
    
    def sumTo(self, r):
        ret = 0
        while r >=0:
            ret += self.bit[r]
            r = (r&(r+1))-1
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx =  idx | (idx +1)

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        pls = [0]
        for x in nums:
            if x %2 ==0:
                pls.append(pls[-1]+b)
            else:
                pls.append(pls[-1]-a)
        vs = sorted(list(set(pls)))
        dic = {val:i for i,val in enumerate(vs)}
        
        ft = FenwickTree([0]*len(vs))
        ret =0 
        
        for i in range(n+1):
            cr = dic[pls[i]]
            ret += i - ft.sumTo(cr-1)
            ft.add(cr,1)
        return ret 
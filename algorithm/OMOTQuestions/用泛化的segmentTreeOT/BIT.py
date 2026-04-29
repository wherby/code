# BIT
# 4.3s



# 针对 Python 性能优化的快捷 max
def fmax(a, b):
    return a if a > b else b

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i: int, val: int):
        i += 1
        while i <= self.n:
            if val > self.tree[i]:
                self.tree[i] = val
            else:
                break
            i += i & (-i)

    def query(self, i: int) -> int:
        i += 1
        res = 0
        while i > 0:
            if self.tree[i] > res:
                res = self.tree[i]
            i -= i & (-i)
        return res

class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        MX =max(nums)+10
        st_up =BIT(MX)
        st_down = BIT(MX)
        ans = 0
        up = [-10**10]*n 
        down =[-10**10]*n 
        for i in range(n):
            a = nums[i]
            if i >=k:
                pidx = i - k 
                pv = nums[pidx]
                st_up.update(MX-pv,up[pidx])
                st_down.update(pv,down[pidx])
            up_val = down_val =a 
            dquery = st_down.query(a-1)
            if dquery != -10**10:
                up_val = max(up_val,dquery + a)
            
            uquery = st_up.query(MX-(a+1))
            if uquery != -10**10:
                down_val = max(down_val,uquery + a)
            
            up[i] = up_val
            down[i] = down_val
            ans = max(ans, up_val,down_val)
        return ans
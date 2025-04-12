from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 

from math import inf

# 标记不下放版本
class SegmentTree:
    def __init__(self,nums):
        n = len(nums)
        self.nums = nums
        
        # 真实值，是否递增，区间左侧值，区间右侧值
        self.f = [[False,-1,-1] for _ in range(4*n)]
        
        self.buildTree(1,0,n-1)
        self.n = n

    def pushup(self,lp,rp):
        lf,a,b = lp
        rf,x,y = rp
        if not lf or not rf:
            return (False,-1,-1)

        if b <= x:
            return (True,a,y)
        else:
            return (False,-1,-1)
    
    # 初始化，求区间和
    def buildTree(self,k,l,r):
        # 叶子节点
        if l == r:
            self.f[k] = (True,self.nums[l],self.nums[l])
            return 
        mid = (l+r)//2
        self.buildTree(2*k,l,mid)
        self.buildTree(2*k+1,mid+1,r)
        
        # 每个k掌管 [2*k,2*k+1]
        self.f[k] = self.pushup(self.f[2*k],self.f[2*k+1])
    
    def update(self,start,end,x):
        return self._update(1,0,self.n-1,start,end,x)
    
    def _update(self,k,l,r,start,end,x):
        # 序号为k的点，掌管范围是l～r， 在区间start～end上，
        # 待更新区间刚好等于当前标准区间，则直接更新
        if l == start and r == end:
            # 肯定递增
            self.f[k] = [True,x,x]
            return
        
        mid = (l+r)//2
            
        if end <= mid: # 只在左子树
            self._update(2*k,l,mid,start,end,x)
             # 注意这里的return
        elif start > mid: # 只在右子树
            self._update(2*k+1,mid+1,r,start,end,x)
        else:
            # 否则对左右子树都需要处理
            self._update(2*k,  l,   mid,   start,mid,x)
            self._update(2*k+1,mid+1,r,    mid+1,end,x) 
        
        # 后缀数组更新，左右子树更新后更新当前子树
        self.f[k] = self.pushup(self.f[2*k],self.f[2*k+1])
    
    def query(self):
        return self.f[1][0]
    
    # 范围内含有1的个数
    def _query(self,k,l,r,start,end):
        # update时对于标准区间已经更新，返回即可
        if l == start and r == end: # 叶子节点
            return self.f[k]
        
        mid = (l+r)//2
        
        # 需要更新，标记下放
        if not self.v[k]:
            self._update(2*k,l,mid,l,mid)
            self._update(2*k+1,mid+1,r,mid+1,r)
            self.v[k] = True
        
        if end <= mid:
            return self._query(2*k,l,mid,start,end) # 注意这里的p已经加上了v[k]的影响
        elif start > mid:
            return self._query(2*k+1,mid+1,r,start,end) 
        
        leftPart = self._query(2*k,l,mid,start,mid)
        rightPart = self._query(2*k+1,mid+1,r,mid+1,end)
        return leftPart + rightPart


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        '''
        相邻和最小的 a,b
        a = a + b
        移除b
        非递减
        1e5
        线段树
        nums[i] nums[j] 合并的话
        相当于
        区间修改 把区间 [i,j] 换成相同的值为 nums[i] + nums[j]
        区间查询 查询整个区间是否递增
        那就是线段树

        快速找最小：
        堆 + 并查集模拟删除
        '''
        n = len(nums)
        # 值，区间 [l,r] 两端点相加
        heap = []

        # 区间合并后，当前 i 的区间范围，-inf 即为被合并了
        area = [ (i,i) for i in range(n) ]
        for i in range(n-1):
            heappush(heap,(nums[i]+nums[i+1],i,i+1))
            
        tree = SegmentTree(nums)
        
        res = 0
        while not tree.query():
            res += 1
            while heap:
                num,l,r = heap[0]
                
                if area[l][1] + 1 != r or nums[l] + nums[r] != num:
                    heappop(heap)
                else:
                    break

            # 操作
            num,l,r = heappop(heap)
            
            # 两个区间
            a,b = area[l]
            x,y = area[r]
            
            # 求和合并
            nums[a] = num
            nums[y] = num
            tree.update(a,y,num)

            
            # 区间合并
            area[b] = area[x] = (-inf,-inf)
            area[a] = (a,y)
            area[y] = (a,y)

            # 和前后区间合并并入堆
            if y + 1 < n and area[y+1][0] != -inf:
                heappush(heap,(num + nums[y+1],l,y+1))

            if a - 1 >= 0 and area[a-1][0] != -inf:
                heappush(heap,(num + nums[area[a-1][0]],area[a-1][0],l))
                
        return res

# 作者：mipha
# 链接：https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/solutions/3641802/xian-duan-shu-dui-by-mipha-2022-l8ui/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


re= Solution().minimumPairRemoval([5,2,3,1])
print(re)
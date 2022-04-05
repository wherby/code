class SegTree:
    def __init__(self, arr):
        m = len(arr)
        n = 1
        while n <m:
            n =n<<1
        self.n = n
        self.tree = [0] *(2*n)
        for i in range(m):
            self.tree[n+i] = arr[i]
        for i in range(n-1,0,-1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def sum(self,a,b):
        a += self.n
        b += self.n
        s =0 
        while a<=b:
            #print(a,b)
            if a %2 ==1:
                s+= self.tree[a]
                a+=1
            if b%2 ==0:
                s += self.tree[b]
                b -=1
            a =a //2
            b = b //2
            #print(a,b,s)
        return s
    
    def add(self,k, x):
        k += self.n
        self.tree[k] +=x
        k = k//2
        while k >=1:
            self.tree[k] = self.tree[2*k] + self.tree[2*k+1]
            k= k//2
    
    def update(self,k,x):
        k += self.n
        self.tree[k] =x
        k = k //2
        while k>=1:
            self.tree[k] = self.tree[2*k] + self.tree[2*k+1]
            k= k//2

class NumArray:

    def __init__(self, nums):
        self.seg= SegTree(nums)

    def update(self, index: int, val: int) -> None:
        self.seg.update(index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self.seg.sum(left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

a = NumArray([1, 3, 5])
re =a.sumRange(0,2)
print(re)
a.update(1,2)
re = a.sumRange(0,2)
print(re)
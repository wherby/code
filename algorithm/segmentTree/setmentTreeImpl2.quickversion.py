#https://usaco.guide/CPH.pdf#page=101
# https://leetcode-cn.com/problems/range-sum-query-mutable/submissions/
# This version will pass other may OT  https://leetcode.cn/contest/weekly-contest-411/problems/count-substrings-that-satisfy-k-constraint-ii/submissions/556410951/
# algorithm/segmentTree/quickVersion
#https://leetcode.cn/contest/weekly-contest-411/problems/count-substrings-that-satisfy-k-constraint-ii/submissions/556410951/


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

a =SegTree([1,2,3,4,5,6])
s = a.sum(2,6)
print(s)
print(a.tree)
a.add(1, 10)
s = a.sum(1,4)
print(s)
print(a.tree)
    
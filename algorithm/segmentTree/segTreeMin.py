import math
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
            self.tree[i] = min(self.tree[2*i] , self.tree[2*i+1])

    def min(self,a,b):
        a += self.n
        b += self.n
        mn = math.inf
        while a<=b:
            #print(a,b)
            if a %2 ==1:
                mn= min(self.tree[a],mn)
                a+=1
            if b%2 ==0:
                mn = min(self.tree[b],mn)
                b -=1
            a =a //2
            b = b //2
        return mn

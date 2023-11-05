class ProductOfNumbers:

    def __init__(self):
        self.num =0
        self.lastValid =0
        self.pre=[1]

    def add(self, num: int) -> None:
        self.num +=1
        if num !=0:
            self.pre.append(self.pre[-1] * num)
        else:
            self.lastValid=self.num
            self.pre =[1]

    def getProduct(self, k: int) -> int:
        if self.num- self.lastValid < k:
            return 0
        else:
            return self.pre[-1] /self.pre[-(k+1)]




# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
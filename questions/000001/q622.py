class MyCircularQueue:

    def __init__(self, k: int):
        self.ls =[0]*k
        self.first=0
        self.last =-1
        self.cnt =0
        self.N = k


    def enQueue(self, value: int) -> bool:
        if self.cnt ==self.N:
            return False
        self.last +=1
        self.last = self.last %self.N
        self.ls[self.last] = value
        self.cnt +=1
        return True


    def deQueue(self) -> bool:
        if self.cnt ==0:
            return False
        self.first +=1
        self.first =(self.first) %self.N
        self.cnt -=1
        return True


    def Front(self) -> int:
        if self.cnt ==0:
            return -1
        return self.ls[self.first]


    def Rear(self) -> int:
        if self.cnt ==0:
            return -1
        return self.ls[self.last]


    def isEmpty(self) -> bool:
        return self.cnt ==0


    def isFull(self) -> bool:
        return self.cnt == self.N


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
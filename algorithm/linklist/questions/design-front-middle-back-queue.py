# https://leetcode.cn/problems/design-front-middle-back-queue/submissions/?envType=daily-question&envId=2023-11-28
from collections import defaultdict,deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque([])
        self.right = deque([])
    
    def balance(self):
        if len(self.left)> len(self.right):
            self.right.appendleft(self.left.pop())
        if len(self.right) > len(self.left) +1 :
            self.left.append(self.right.popleft())


    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()


    def pushMiddle(self, val: int) -> None:
        self.left.append(val)
        self.balance()


    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()


    def popFront(self) -> int:
        if len(self.left) == 0:
            if len(self.right)>0:
                return self.right.popleft()
            else:
                return -1
        else:
            a =self.left.popleft()
            self.balance()
            return a 
    def popMiddle(self) -> int:
        if len(self.right)>0:
            if len(self.left) == len(self.right):
                return self.left.pop()
            return self.right.popleft()
        else:
            return -1 


    def popBack(self) -> int:
        if len(self.right) ==0:
            return -1 
        else:
            a = self.right.pop()
            self.balance()
            return a 


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
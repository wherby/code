

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class PersistentArray:
    def __init__(self):
        self.L=0
        self.R=2*10**5
        self.M = 20* 2* 10**5
        self.pool = [Node(-1) for _ in range(self.M)]

print(30*10**4)
a = PersistentArray()
print(len(a.pool))


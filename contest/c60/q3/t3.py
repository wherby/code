class LockingTree:

    def __init__(self, parent):
        n = len(parent)
        self.tree =[]
        for i in range(n):
            self.tree.append([-1,[],-1])
        for i in range(n):
            pi = parent[i]
            self.tree[i][0] =pi
            if pi != -1:
                self.tree[pi][1].append(i)
        #print(self.tree)

    def lock(self, num: int, user: int) -> bool:
        #print(self.tree)
        if self.tree[num][2]  == -1:
            self.tree[num][2] = user
            return True
        else:
            return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.tree[num][2] == user:
            self.tree[num][2] = -1
            #print(num,user)
            return True
        else:
            return False
        

    def upgrade(self, num: int, user: int) -> bool:
        if self.tree[num][2] ==-1:
            child = []
            parent= []
            tp = num
            while self.tree[tp][0] != -1:
                parent.append(self.tree[tp][0])
                tp = self.tree[tp][0]
            parentLock = list(filter(lambda x : self.tree[x][2] != -1,parent))
            if len(parentLock) >0:
                return False
            else:
                tpChild = self.tree[num][1]
                while len(tpChild)>0:
                    child = child + tpChild
                    res =[]
                    for ch in tpChild:
                        res += self.tree[ch][1]
                    tpChild =res
                childLock = list(filter(lambda x : self.tree[x][2] !=-1,child))
                if len(childLock) ==0:
                    return False
                else:
                    for c in childLock:
                        self.tree[c][2] = -1
                    self.tree[num][2] =user
                    return True
        else:
            return False


# Your LockingTree object will be instantiated and called as such:
obj = LockingTree([-1,5,5,5,0,4,2,9,0,4])
param_1 = obj.lock(5,12)
param_2 = obj.unlock(5,12)
obj.upgrade(3,7)
obj.upgrade(7,27)
obj.upgrade(9,42)

obj.unlock(6,37)
obj.lock(8,24)
obj.upgrade(8,27)
obj.lock(8,13)
obj.unlock(8,24)
obj.upgrade(2,22)
rr= obj.lock(5,38)
print(param_1,param_2,rr)
#param_3 = obj.upgrade(num,user)
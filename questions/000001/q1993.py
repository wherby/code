from typing import List, Tuple, Optional
class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.g=[[] for _ in range(n)]
        for i,a in enumerate(parent):
            if a != -1:
                self.g[a].append(i)
        self.lk = [0]*n
        #print(self.g)

    def lock(self, num: int, user: int) -> bool:
        if self.lk[num] ==0:
            self.lk[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.lk[num] == user:
            self.lk[num] = 0 
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        isPG= True
        cur = num
        while self.parent[cur] != -1:
            if self.lk[cur] !=0:
                isPG = False
            cur = self.parent[cur]
        if self.lk[cur] !=0:
            isPG = False
            #print(cur)
        isCL = False
        def dfs(node):
            nonlocal isCL
            if self.lk[node]>0:
                isCL = True
            for a in self.g[node]:
                dfs(a)
        def dfs2(node):
            self.lk[node] =0
            for a in self.g[node]:
                dfs2(a)
        for a in self.g[num]:
            dfs(a)
        if isPG and isCL:
            dfs2(num)
            self.lk[num] = user
            return True
        return False


# Your LockingTree object will be instantiated and called as such:
obj = LockingTree([-1,0,3,1,0])
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
obj.upgrade(4,5)
#obj.upgrade(3,8)
#obj.unlock(0,7)
#obj.lock(2,7)
#obj.upgrade(4,6)
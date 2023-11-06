from collections import defaultdict
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dic = defaultdict(list)
        self.root = kingName
        self.deathM = {}


    def birth(self, parentName: str, childName: str) -> None:
        self.dic[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deathM[name] = 1


    def getInheritanceOrder(self) -> List[str]:
        res =[]
        def dfs(name):
            if name not in self.deathM:
                res.append(name)
            for k in self.dic[name]:
                dfs(k)
        dfs(self.root)
        return res



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
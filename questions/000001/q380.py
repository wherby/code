from random import Random, random


class RandomizedSet:

    def __init__(self):
        self.s1 = set([])


    def insert(self, val: int) -> bool:
        if val in self.s1:
            return False
        else:
            self.s1.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.s1:
            self.s1.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        n = len(self.s1)
        x = random.choice(self.s1)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
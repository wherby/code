from random import randrange

from tombola import Tombola

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pop from empty TomboList")
    
    load = list.extend
    print("init")

    def loaded(self):
        return bool(self)
    
    def inspect(self):
        return tuple(sorted(self))

a1 =TomboList()
a2 = TomboList()
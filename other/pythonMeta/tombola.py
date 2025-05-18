import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self,iterable):
        """从迭代返回元素"""
    
    @abc.abstractmethod
    def pick(self):
        """
        随机返回， 空返回Error
        """
    
    def load(self):
        return bool(self.inspect())
    
    def inspect(self):
        items =[]
        while True:
            try:
                items.append(self.pick)
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
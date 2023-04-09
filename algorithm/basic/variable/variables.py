


class Connection:
    def __init__(self) -> None:
        self.value={}
        pass
    #value={}

class Solution:
    def __init__(self):
        pass
        #self.zone  =Connection()
    full= 1
    zone  =Connection()
    def show(self):
        print(self.zone.value)
        

a= Solution()
b=Solution()
print((a.zone))
print(b.zone)
print(Solution.zone)

a.zone.value["x"] =1
a.full =2

a.show()
b.show()
print(a.full,b.full)
print(a.__dict__,b.__dict__)
print(Solution.__dict__)

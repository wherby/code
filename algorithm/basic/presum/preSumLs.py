class PresumLs:
    def __init__(self,ls):
        n = len(ls)
        self.pre = [0]*(n+1)
        for i in range(n):
            self.pre[i+1] = self.pre[i] + ls[i]
a =[0,1,2,4]
pre = PresumLs(a)
print(pre.pre)
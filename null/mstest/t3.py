class PriceApp:
    def __init__(self) -> None:
        self.dic={}
    def setPrice(self,item,price):
        if item not in self.dic:
            self.dic[item]=[0,0,[]]
        self.dic[item][1] =price
    def setFormula(self,item, a,b,c):
        if item not in self.dic:
            self.dic[item] = [0,0,[]]
        self.dic[item][2] = [a,b,c]
    def setNum(self,item,num):
        if item not in self.dic:
            self.dic[item] =[0,0,[]]
        self.dic[item][0] = num
    def getPrice(self,item):
        if item not in self.dic:
            return "Not found"
        else:
            if len(self.dic[item][2]) ==0:
                return self.dic[item][0] * self.dic[item][1]
            else:
                a,b,c = self.dic[item][2]
                return a * self.getPrice(b) +c
    def queryPrice(self,price):
        res =[]
        for item,v in self.dic.items():
            if v[1] >= price:
                res.append(item)
        return res
    def getBasket(self, bls):
        res =0
        for item in bls:
            t = self.getPrice(item)
            print(item  ," with price: ", t)
        pass

# from bisect import bisect_right,insort_left,bisect_left
# a=[1,2,3,4,5]
# idx =bisect_left(a,4)
# print(idx)
# lg(n) -n*m
# n -n*m
#log(n)
a = PriceApp()
a.setPrice("app",2)
a.setNum("app",103)
re = a.getPrice("app")
print(re)
re=a.getPrice("or")
print(re)
a.setNum("or",-10000000000000000000000000000)
a.setNum("or", 0.1 **19)
a.setPrice("or",1999)
re = a.getPrice("or")
print(re)
a.setFormula("or",0.1,"app",3)
re = a.getPrice("app")
print("app: " ,re)
bs =["app","or"]
a.getBasket(bs)

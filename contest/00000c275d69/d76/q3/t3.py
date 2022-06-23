
class ATM(object):

    def __init__(self):
        self.cls = [20,50,100,200,500]
        self.ls = [0]*5

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i,a in enumerate(banknotesCount):
            self.ls[i] +=a


    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        ret =[0]*5
        for i in range(4,-1,-1):
            if amount>= self.cls[i]:
                t = min(amount //self.cls[i], self.ls[i])
                amount = amount -self.cls[i]*t
                ret[i] =t
        if amount ==0:
            for i in range(5):
                self.ls[i] -=ret[i]
            return ret 
        return [-1]





from collections import defaultdict


class DiscountSystem(object):

    def __init__(self):
        self.disc =[]
        self.userUse = defaultdict(int)

    def addActivity(self, actId, priceLimit, discount, number, userLimit):
        """
        :type actId: int
        :type priceLimit: int
        :type discount: int
        :type number: int
        :type userLimit: int
        :rtype: None
        """
        self.disc.append([actId,priceLimit,discount,number,userLimit])


    def removeActivity(self, actId):
        """
        :type actId: int
        :rtype: None
        """
        self.disc = list(filter(lambda x: x[0] != actId,self.disc))


    def consume(self, userId, cost):
        """
        :type userId: int
        :type cost: int
        :rtype: int
        """
        mx =0
        ddix = -1
        for i,disc in enumerate(self.disc):
            if cost >= disc[1] and self.userUse[str(userId) +"@"+ str(disc[0])] < disc[4] and disc[3] >0:
                if disc[2] > mx :
                    mx = disc[2] 
                    ddix = i
        if ddix != -1:
            self.userUse[str(userId) +"@"+ str(self.disc[ddix][0])]+=1
            self.disc[ddix][3] -=1
            return cost- self.disc[ddix][2]
        else:
            return cost


class Bitset(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size =size 
        self.ls = [0]*size
        self.cnt = 0
        self.fn = 0


    def fix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if self.ls[idx] ==0 and self.fn %2 ==0:
            self.cnt +=1
            self.ls[idx] =1
        elif self.ls[idx] ==1 and self.fn%2 ==1:
            self.cnt -=1
            self.ls[idx] =0



    def unfix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if self.ls[idx] ==1 and self.fn %2 ==0:
            self.cnt -=1
            self.ls[idx] =0
        elif self.ls[idx] ==0 and self.fn %2 ==1:
            self.cnt  +=1
            self.ls[idx] =1


    def flip(self):
        """
        :rtype: None
        """
        self.fn +=1


    def all(self):
        """
        :rtype: bool
        """
        if self.fn %2 ==0:
            return self.cnt == self.size
        else:
            return self.cnt  ==0
    def one(self):
        """
        :rtype: bool
        """
        if self.fn %2 ==1:
            return self.cnt != self.size
        else:
            return self.cnt  !=0

    def count(self):
        """
        :rtype: int
        """
        if self.fn %2 ==0:
            return self.cnt 
        else:
            return self.size- self.cnt


    def toString(self):
        """
        :rtype: str
        """
        re = ""
        if self.fn %2 ==0:
            for i in range(self.size):
                if self.ls[i] ==0:
                    re = re + "0"
                else:
                    re = re + "1"
        else:
            for i in range(self.size):
                if self.ls[i] ==0:
                    re = re + "1"
                else:
                    re = re + "0"
        return re
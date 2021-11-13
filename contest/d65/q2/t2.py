class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.n = width
        self.m = height
        self.p = [0,0]
        self.dir = 0
        self.dics =[[1,0],[0,1],[-1,0],[0,-1]]
        self.cir = (width + height -2) *2


    def move(self, num):
        """
        :type num: int
        :rtype: None
        """
        dicT = self.dics[self.dir]
        x,y = self.p
        num = num % self.cir + self.cir
        while num >0:
            xn =x+ dicT[0] *num
            yn =y+ dicT[1] *num
            if xn>=0 and xn < self.n and yn >=0 and yn <self.m:
                x= xn
                y= yn
                num =0
            else:
                if dicT[0] ==0:
                    if dicT[1] >0:
                        num1 = self.m-1-y
                        y=self.m-1
                        num = num-num1
                    else:
                        num =num -y
                        y=0
                else:
                    if dicT[0]>0:
                        num1 = self.n -1 -x
                        x = self.n -1
                        num = num -num1
                    else:
                        num = num -x
                        x =0
                self.dir = (self.dir +1)%4
                dicT = self.dics[self.dir]
            #print(x,y,xn,yn,dicT)
        self.p = [x,y]


    def getPos(self):
        """
        :rtype: List[int]
        """
        return self.p

    def getDir(self):
        """
        :rtype: str
        """
        if self.dir == 0:
            return "East"
        if self.dir ==1:
            return "North"
        if self.dir ==2:
            return  "West"
        if self.dir ==3:
            return  "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

robot = Robot(6, 3)
robot.move(2)
robot.move(2)
re =robot.getPos()
print(re)
re= robot.getDir()
re=robot.move(2)
print(re)             
robot.move(1)  
robot.move(4) 
               
re=robot.getPos()
print(re)
re=robot.getDir()
print(re)
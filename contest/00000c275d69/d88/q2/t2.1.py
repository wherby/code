class LUPrefix(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.dic ={}
        self.mx =1


    def upload(self, video):
        """
        :type video: int
        :rtype: None
        """
        self.dic[video] =1


    def longest(self):
        """
        :rtype: int
        """
        while self.mx in self.dic:
            self.mx +=1
        return self.mx -1


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()



a = LUPrefix(4)
re =a.upload(3)
print(a.longest())
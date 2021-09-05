class class1(object):
    class class2:
        def printS(self):
            print "Inside Class2"
    def fun1(self):
        c2 = self.class2()
        c2.printS()

c1 = class1()
c1.fun1()


#Inside Class2
#[Finished in 0.1s]
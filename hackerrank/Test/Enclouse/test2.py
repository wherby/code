class class1(object):
    class class2:
        def printS(self):
            print "Inside Class2"
    def fun1(self):
        c2 = class2()
        c2.printS()

c1 = class1()
c1.fun1()

#  File "C:\Users\where\Documents\github\hackerrank\Test\Enclouse\test2.py", line 10, in <module>
#    c1.fun1()
#  File "C:\Users\where\Documents\github\hackerrank\Test\Enclouse\test2.py", line 6, in fun1
#    c2 = class2()
#NameError: global name 'class2' is not defined
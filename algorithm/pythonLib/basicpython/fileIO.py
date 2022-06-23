import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

f2 = open("./input01.out.txt", "a")
a,b=1,2
f2.writelines([str(a) + " " +str(b)+"\n"])
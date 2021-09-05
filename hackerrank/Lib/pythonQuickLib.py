#sorted with index:
myList = [1, 2, 3, 100, 5]
index = [i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]
print(index)

# compare with cmp function
#suffixes= sorted(suffixes, cmp = lambda x,y: compsuff(x,y))   Used in python2
# 
import functools
qls = [5, 2, 4, 1, 3]
def cmp(x,y):
    if x>y:
        return -1  # @@@@@@ return False will not work
    else:
        return 1

qls2 =  sorted(qls, key=functools.cmp_to_key(cmp))  ##Used in python3
print(qls2)



## Python2 will a/b => python3  a //b


##Python2:
#vls= map(int , ins[index+1].strip().split())

##Python3:
#vls= list(map(int , ins[index+1].strip().split()))
#vls[i] only visited when cast to list
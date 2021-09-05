inf = float("inf")
ninf = float("-inf")



from collections import defaultdict
dd = defaultdict(list)

def zero():
    return 0
dd2 = defaultdict(zero)



a= True
print [1,2][1 >3], [1,2][4>3]
print 4 if 2>4 else 2

ls = [1]

##this will not pass **********************
#print [ls[2],ls[0]][0>2]
print ls[2] if 0 >2 else ls[0]
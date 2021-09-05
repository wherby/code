#// array, 'a', 'b', 'c'
#// unsorted
#// input -> ['b', 'a', 'b', 'a', 'c', 'a']
#// output ->


def sortls(ls):
    pa,pb,pc = 0,0,0
    n =len(ls)
    for i in range(n):
        t= ls[i]
        if t == 'a':
            pa = pa +1
        if t =='b':
            pb = pb +1
        if t == 'c':
            pc = pc +1
    
    print ls






ls =['b', 'a', 'b', 'a', 'c', 'a']
sortls(ls)
pb =0
pa =-1
pa =1

['a', 'b', 'b', 'a', 'c', 'a']
pb = 1
pa =3
['a', 'a', 'b', 'b', 'c', 'a']
pb =2
pa =5
pc =4
['a', 'a', 'a', 'b', 'c', 'b']
pb =3
pa =2
pc =4
['a', 'a', 'a', 'b', 'c', 'b']
pb =5
pa =2
pc =4
['a', 'a', 'a', 'b', 'b', 'c']
# There are n points on a 2d plane, could you found a symmetry line that is parallel to y-axis to apply all the points?
##eg, 
#input: [1, 1], [3, 1], [5, 6], [-1, 6]
#output: true

#input: [1, 1], [3, 1], [5, 6], [-1, 6], [4, 3], [1, 3]
#output: false


def findSym(poinits):
    a1 =0
    b1 = poinits[0][1]
    cnt =0
    dic1 ={}
    for point in poinits:
        x,y = point
        dic1[(x,y)]=1
        if y == b1:
            a1 = a1 + x 
            cnt = cnt +1
    xSym = a1/cnt
    isSym = True
    for point in poinits:
        x,y = point
        x1,y1 = xSym*2 - x, y
        if (x1,y1) not  in dic1:
            isSym =False
            break
    #print isSym
    #print cnt, a1,x
    return isSym



poinits = [[1, 1], [3, 1], [5, 6], [-1, 6]]
print findSym(poinits)
poinits2 = [[1, 1], [3, 1], [5, 6], [-1, 6], [4, 3], [1, 3]]
print findSym(poinits2)


#True
#False

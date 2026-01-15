

def getXHighBit(x):
    bit = x.bit_length()
    v = (1<<bit) -1
    print(v^x, 1<<bit-1)


getXHighBit(14)
getXHighBit(222)
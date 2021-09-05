
def transValueInGet(a):
    return [str(x) for x in a]

def mapValue(a):
    return [str(x) for x in a]

def typesafeMapValue(a):
    if a == None:
        return None
    else:
        return mapValue(a)

test1 = None
test2 = [1,None,2]

#mapValue(test1)
#transValueInGet(test1)

def typeSafeMap(a, mapFun):
    if a == None:
        return None
    else:
        return mapFun(a)


typesafeMapValue(test1)
print typeSafeMap(test1,mapValue)
print typeSafeMap([1,2,3,],mapValue)


print mapValue(test2)


def safeMap(func):
    def wrapper(*arg,**kw):
        if arg[0] == None:
            return None
        else:
            return func(*arg,**kw)
    return wrapper



@safeMap
def mapValue2(a):
    return [str(x) for x in a]

print mapValue2(None)
print mapValue2(test2)

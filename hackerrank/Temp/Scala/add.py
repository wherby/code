def addInt(input):
    if "a" in input and "b" in input:
        a = input["a"]
        b = input["b"]
        try:
            int(a)
            try:
                int(b)
                return a+b
            except:
                print b + " is not int"
        except:
            print a + " is not int"
    else:
        print "a or b not in input parameters"

    


print addInt({"a":1,"b":2})
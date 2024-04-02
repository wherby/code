a = {"a":14}

def updateData(obj):
    if "time" in obj:
        obj["time"] = 15
        return obj
    return obj 

print(updateData(a))
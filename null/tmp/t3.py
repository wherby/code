names = ["Fund Aduit", "PEVC"]

Warning1Name = {
    "PEVC": "company"
}

def getNameWarning1(name):
    return Warning1Name.get(name, name)

def frontendToDBMappeing():
    namesDB = ["_".join(a.split(" ")).lower() for a in names]
    dic = {}
    for a,b in zip(names,namesDB):
        dic[a]=b 
    print(dic)

print(getNameWarning1("PEVC"))
frontendToDBMappeing()
print(getNameWarning1("Fund audit"))
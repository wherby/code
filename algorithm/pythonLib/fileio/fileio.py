import pickle
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def saveTo(file,obj):
    with open(file,"wb") as outp:
        pickle.dump(obj,outp, pickle.HIGHEST_PROTOCOL)

def loadFrom(file):
    with open(file,"rb") as inp:
        obj = pickle.load(inp)
        return obj



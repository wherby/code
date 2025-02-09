


FILEDEBUG =True
if FILEDEBUG:
    import os

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/debug.txt', 'w')
    sys.stdout = f

    #Start print
    #print(ret2)
    #ret2[1]=[1]
    # re =Solution().minCostGoodCaption(caption ="ylrtdmm")
    # print(re)

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    print("finished")

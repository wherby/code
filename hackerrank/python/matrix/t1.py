import re
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in xrange(n):
    matrix_t = str(raw_input())
    matrix.append(matrix_t)
ret= ""
for j in range(m):
    for i in range(n):
        ret = ret +matrix[i][j]

b = "([A-Z,a-z,0-9]+[^A-Z,a-z,0-9]*[A-Z,a-z,0-9]+)(([^A-Z,a-z,0-9]*[A-Z,a-z,0-9]+)*)"
m=re.search(b,ret)
try:
    ma= m.group(0)
    gs = m.groups()
    start = ret.find(ma)
    prefix = ret[:start]
    postfix = ret[start+len(ma):]
    b1 =  "([A-Z,a-z,0-9]+)([^A-Z,a-z,0-9]*)([A-Z,a-z,0-9]+)"
    m1 = re.match(b1,gs[0]).groups()
    ret2 = prefix
    ret2 = prefix + m1[0] + " " + m1[2]

    b2 = "([^A-Z,a-z,0-9]+[A-Z,a-z,0-9]+)"

    m2 = re.findall(b2,gs[1])
    for i in range(len(m2)):
        c3 = "([^A-Z,a-z,0-9]+)([A-Z,a-z,0-9]+)"
        c2 = re.match(c3,m2[i]).groups()
        ret2 = ret2 +" " +c2[1]
    ret2 = ret2  + postfix 
    ret2.rstrip()
except:
    ret2 = ret
print ret2
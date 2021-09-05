#https://docs.python.org/2/library/heapq.html
import heapq

a=[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(a)
print(a)

c=[]

for i in range(len(a)):
    b= heapq.heappop(a)
    print(b)
    heapq.heappush(c,b)
print(c)

print("=======heap replace====")
d = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heapq.heapify(d)
print(d)
heapq.heapreplace(d,2)  # prop one and add item to heap
print(d)

pushpop= heapq.heappushpop(d,-1)
print(pushpop)

print("========heap merge multiple sorted inputs , the inputs must be sorted==========")
a =[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
b =[2,5,7,8,10]
heapq.heapify(a)
heapq.heapify(b)
c= heapq.merge(a,b)
d = []
for x in c:
    d.append(x)
print("d is not sorted:")
print(d)

a = [heapq.heappop(a) for i in range(len(a))]

c= heapq.merge(a,b)
d = []
for x in c:
    d.append(x)
print("d is sorted:")
print(d)

print("+==========heapq nlargest=======")
large4 =heapq.nlargest(4, d)
small3 = heapq.nsmallest(3,d)
print("largest 4 in {} is {}  and 3 smallest  is {}".format(d,large4,small3))

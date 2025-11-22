

a = 12

d = 1 
newMsk = a | (1<<d)
print(newMsk,newMsk%(1<<d),  newMsk//(1<<d))
newMsk = newMsk//(1<<d) + ((newMsk%(1<<d))<<(5-d))
print(bin(newMsk),newMsk)

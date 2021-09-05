
import time,random
from threading import Thread

a=[1,2,3,4]
for i in a:
	time.sleep(random.randrange(10))
	print i
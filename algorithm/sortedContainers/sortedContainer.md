# SortedContainer has both quick insert and delete and sorted feature
https://www.youtube.com/watch?v=Lcli3vUr7Yc
#
https://www.youtube.com/watch?v=7z2Ki44Vs4E --- Grant Jenks - Python Sorted Collections - PyCon 2016
from sortedcontainers import SortedSet

# link 
http://www.grantjenks.com/docs/sortedcontainers/sortedlist.html
http://www.grantjenks.com/docs/sortedcontainers/introduction.html#sorted-dict
http://www.grantjenks.com/docs/sortedcontainers/introduction.html#sorted-set
http://www.grantjenks.com/docs/sortedcontainers/introduction.html


# Sortedlist
http://www.grantjenks.com/docs/sortedcontainers/sortedlist.html

>>> sl = SortedList([1, 2, 3, 4, 5,5])  
>>> sl.discard(5)
>>> sl
SortedList([1, 2, 3, 4, 5])
>>> sl.pop(-1)
5
>>> sl
SortedList([1, 2, 3, 4])
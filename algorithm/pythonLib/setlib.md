https://sparkbyexamples.com/python/python-remove-set-element-if-exists/#:~:text=Element%20if%20Exists-,The%20set.,then%20%E2%80%9CKeyError%E2%80%9D%20is%20returned.

4. Difference between remove() & discard()

remove() is a method that will raise an error if we try to remove an element that doesn’t exists in an iterable.	
discard() is a method that will not raise an error if we try to remove an element that doesn’t exist in an iterable.
It is better to use a try-except block while using the remove() method or handle the exception.	There is no need to handle exceptions.
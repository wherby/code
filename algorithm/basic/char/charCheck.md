
## char isalpha
e.isalpha() 
e.isdigit()

val.islower()
val.upper()

print(v.lower())
print(v.capitalize())
isLow = any(c.islower() for c in password)
isBig = any(c.isupper() for c in password)
isDig =any(c.isdigit() for c in password)



## aToZ
import string
print list(string.ascii_lowercase)

small_letters = map(chr, range(ord('a'), ord('z')+1))
big_letters = map(chr, range(ord('A'), ord('Z')+1))
digits = map(chr, range(ord('0'), ord('9')+1))

import string
string.letters
string.uppercase
string.digits

ABC = ['abcdefghijklmnopqrstuvwxyz']

from string import ascii_lowercase


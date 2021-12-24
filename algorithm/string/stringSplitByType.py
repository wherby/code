import re
ptn = re.compile(r'[a-z]+|[1-9]+')

str1 = "ab123cd345"
s1 = ptn.findall(str1)
print(s1)
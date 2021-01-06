import re
a = 'HEY man, wassup?'
b = re.sub('[A-Z]', '', a)
print(b)

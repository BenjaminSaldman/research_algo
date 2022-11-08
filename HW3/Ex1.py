import re

regex = r'\b[A-Za-z0-9+.-_{0,1}A-Za-z0-9+]+@[A-Za-z0-9+.-_{1,1}A-Za-z0-9+]+\.[A-Z|a-z]{2,}\b'

print(re.fullmatch(regex, 'abc-@mail.com'))
print()

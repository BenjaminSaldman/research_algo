import re

regex = r'\b[A-Za-z0-9+.%-_{0,1}A-Za-z0-9+]+@[A-Za-z0-9+.-_{1,1}A-Za-z0-9+]+\.[A-Z|a-z]{2,}\b'
#regex = r'\b(A-Z|a-z|0-9)(A-Z*a-z*0-9*)[+.%-_](A-Z|a-z|0-9)(A-Z*a-z*0-9*)+@[A-Za-z0-9+.-_{1,1}A-Za-z0-9+]+\.[A-Z|a-z]{2,}\b'
regex=r'\b([A-Za-z0-9]+([A-Za-z0-9]*[._-][A-Za-z0-9])*[A-Za-z0-9]+)+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b'
print(re.fullmatch(regex, 'abc%a.aaaa@mail.com'))
print()


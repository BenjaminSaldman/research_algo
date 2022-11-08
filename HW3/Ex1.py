import re

# regex of valid email address according to: https://help.xmatters.com/ondemand/trial/valid_email_format.htm
regex = r'\b([A-Za-z0-9]+([A-Za-z0-9]*[._-][A-Za-z0-9])*[A-Za-z0-9]*)+@([A-Za-z0-9]+([A-Za-z0-9]*[._-][A-Za-z0-9])*[A-Za-z0-9]*)+\.[A-Za-z]{2,4}\b'
filename = input("Please enter the file name: ")
"""
I assumed that each row contains 1 mail address.
file.txt contains all the mail addresses that appearing in: https://help.xmatters.com/ondemand/trial/valid_email_format.htm
"""
with open(filename, mode='r') as file:
    text = file.readlines()
valid = []
invalid = []

for i in text:
    i = i.strip('\n\t\b')  # Ignore special characters.
    if re.fullmatch(regex, i) is None:
        invalid.append(i)
    else:
        valid.append(i)

print(f"Valid: {valid}")
print(f"Invalid: {invalid}")

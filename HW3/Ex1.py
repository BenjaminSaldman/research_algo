import re
import doctest

# regex of valid email address according to: https://help.xmatters.com/ondemand/trial/valid_email_format.htm
# Helped with: https://www.codexpedia.com/regex/regex-symbol-list-and-regex-examples/
regex = r'\b([A-Za-z0-9]+([A-Za-z0-9]*[._-][A-Za-z0-9])*[A-Za-z0-9]*)+@([A-Za-z0-9]+([A-Za-z0-9]*[._-][A-Za-z0-9])*[A-Za-z0-9]*)+\.[A-Za-z]{2,}\b'


def Ex1(filename: str):
    """
    I assumed that each row contains 1 mail address.
    file.txt contains all the mail addresses that appearing in: https://help.xmatters.com/ondemand/trial/valid_email_format.htm
    >>> Ex1("file.txt")
    Valid: ['abc-d@mail.com', 'abc.def@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com']
    Invalid: ['abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com', 'abc..def@mail.com', 'abc.def@mail..com']
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


if __name__ == '__main__':
    doctest.testmod()
    filename = input("Please enter the file name: ")
    Ex1(filename)

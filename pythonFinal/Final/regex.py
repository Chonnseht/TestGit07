def re01():
    import re

    names = ['Finn Bindeballe',
             'Geir Anders Berge',
             'HappyCodingRobot',
             'Ron Cromberge',
             'Sohil']

    # Find people with first and last name only
    regex = r'^\w+\s+\w+$'
    for name in names:
        result = re.search(regex, name)
        if result:
            print(name)

    # Search for word char sequence starting with C
    regex = r'C\w*'
    for name in names:
        match = re.search(regex, name)
        if match:
            print(name)
            print(match.span())

def re02():
    import re
    names = ['Brian Daugette',
             'Veronica Supersonica',
             'Tony Gasparovic',
             'Patrick Germann',
             'm!sha']
    # Test for first name and last name 2nd method using group()
    regex = r'^(?P<fn>\w+)\s+(?P<ln>\w+)$'
    for name in names:
        match = re.search(regex, name)
        if match:
            print(name)
            print(match.group('fn'))
            print(match.group('ln'))

    # Detect last name
    regex = r'^[a-zA-Z!]+$'
    for name in names:
        if re.search(regex, name):
            print(name)

    # Scan for blocks of lower case letters
    #return all non-overlapping matches of pattern in string,
    #   as a list of strings, as a list of strings or tuples
    regex = r'[a-z]+'
    for name in names:
        matches = re.findall(regex, name)
        if matches:
            print(matches)

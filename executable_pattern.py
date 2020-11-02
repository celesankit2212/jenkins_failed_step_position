import re


def usable_patterns():
    
    first_pattern = re.compile(r'(?:)\d+:\d+:\d+\s.+/(\w+.py)\s(.+)\s\[.+\]')
    second_pattern = re.compile(r'(?:)\d+:\d+:\d+\s+[^\w+](.+)\s+\[.+\]')

    return first_pattern, second_pattern


if __name__ == '__main__':
    usable_patterns()

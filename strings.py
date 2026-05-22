# String datatype
# A string consists of characters
sample_str = "Welcome to python session"

# A string is an array of characters
# How to access individual elements in an array?
# Python is zero index based, -ve index based

first_char = sample_str[0]
# print(first_char)

last_char = sample_str[-1]
# print(last_char)

str_len = len(sample_str)
# print(str_len)

words = sample_str.split(sep=" ") # list
# print(words, type(words))

# print(dir(sample_str))

"""
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""

sample_str = " hello, welcome to python "
# print(sample_str.strip())

sample_str = "Welcome to python session"

# How to extract first 2 characters of sample_str
# To do this, we use ':' -> slicing
# Usage: start:end:step, all three are optional
# Important: end index is not included, hence use end+1
first_two = sample_str[0:5] # here the step size value is 1 (default)
print(first_two)

alternate_chars = sample_str[::2] # start: 0, end: len(str)
print(alternate_chars)

# Reverse a string
reverse_string = sample_str[::-1] # start: -1, end: -1-len(str), step: -1
print(reverse_string)

sample_str = "Welcome to python session"
# sample_str[2] = 'a' # Throws an error: 'str' object does not support item assignment
# The above error indicates that its an immutable datatype
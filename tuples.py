my_tuple = ("apple", "banana", "orange", "mango")
# print(my_tuple, my_tuple[0], my_tuple[-1])

# Tuple once defined can't be alerted where as a list can be altered
# print(dir(my_tuple))

# ['count', 'index']
print(my_tuple.index("orange"))

# my_tuple.append("abc") # Throws an error: 'tuple' object has no attribute 'append'

# Tuple is an immutable datatype, similarly strings are also immutable 
# List is a mutable datatype

sample_str = "Welcome to python session"
# sample_str[2] = 'a' # Throws an error: 'str' object does not support item assignment
# The above error indicates that its an immutable datatype

# my_tuple.append("abc") # Throws an error: 'tuple' object has no attribute 'append'
# The above error indicates that its an immutable datatype

fruits = ["apple", "banana", "orange", "mango", 1, 2, 3, True]
fruits.append(5)
print(fruits)
# The original list is altered, hence its a mutable datatype
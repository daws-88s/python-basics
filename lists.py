# List is a heterogenous datatype
fruits = ["apple", "banana", "orange", "mango", 1, 2, 3, True]
# print(fruits[0], fruits[-1])
# print(fruits[0:2])
# print(len(fruits))
# print(dir(fruits))

"""
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""
# append: Add elements to a list "at end"
# If the output of an operation is None, then its an inplace operation
fruits1 = fruits.append(5)
# print(fruits, fruits1)

# Iterable: Something you can iterate on
# 'int' object is not iterable
# fruits.extend(6) # Throws an error

fruits.extend("6")
# print(fruits)

fruits.append(["apple", "banana", "orange", "mango"])
# print(fruits)
fruits.extend(["apple", "banana", "orange", "mango"])
# print(fruits)

# Append vs extend
# Append operation adds the entire element as-is
# Extend operation iterates over the iterable and appends the element to the original list

# print(fruits.count("apples"))
# mango_index = fruits.index("mango")
# print(mango_index)
# print(fruits[::-1])

sample_str = "Welcome to python session"
sample_str_list = list(sample_str) # typecasting: converting one datatype to another datatype
# print(sample_str_list)

sample_str_list = "".join(list(sample_str)) # typecasting: converting one datatype to another datatype
# print(sample_str_list)

sample_list = [1, 2, 3, 5, 4, 6]
# sample_list.sort() # inplace operation
print(sample_list)

sample_list_stored = sorted(sample_list)
print(sample_list, sample_list_stored)

# .sort() is an inplace operation and sorted() returns the sorted list
my_dict = {} # dict()
# print(type(my_dict))

# A dictonary consists of key-value pairs
my_dict = {"a": 1, 2: "b", 3: True}
print(my_dict)

# my_dict = {"a": 1, 2: "b", 3: True, ['a', 'b']: 123} # Throws an error: cannot use 'list' as a dict key (unhashable type: 'list')
# print(my_dict)

# Keys should of immutable dataype
# mutable vs immutable
# Mutable: once defined -> can be altered, hence list can't be a key
# Immutable: Once defined -> can't be altered, hence tuples and string can be keys

my_dict = {"a": 1, 2: "b", 3: True}
print(my_dict["a"], my_dict.get(2))
# .get() returns None if the key is not present in the dictonary

my_dict["a"] = 10 # Original dictonary is altered
print(my_dict) 
# Hence dictonary is a mutable dataype

# print(dir(my_dict))
"""
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""
print(my_dict.items()) # Returns a list of tuples with key and value as each element
print(my_dict.keys()) # Returns keys as a list
print(my_dict.values()) # Returns values as a list
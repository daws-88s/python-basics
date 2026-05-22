sample = set()
# print(sample, type(sample))
# A set consists of unique values only and is an unordered collection
# Because of this a set does not support indexing
sample = {'a', 'a', 'b', 'c'}
# print(sample)

# print(sample[0]) # 'set' object is not subscriptable

# print(dir(sample))

"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
"""
sample.add(1) # This proves, set is a mutable datatype
# print(sample)

set1 = {'a', 'a', 'b', 'c', 'z'}
set2 = {1, 'a', 'b', 'c'}
print(set1, set2)
print(set1.intersection(set2)) # Find the common elements between set1 and set2
print(set1.difference(set2)) # Return the difference between set1 and set2
set1.difference_update(set2) # Find the difference and update the set1
print(set1)
all_elements = set1.union(set2)
print(set1, set2, all_elements)
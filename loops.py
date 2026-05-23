# Loops in Python
# For loop, while loop

# Print values from 1 to 10
# If the value is equal to 5, don't print 
# continue, break 
# If the value is equal to 6, halt the execution 

# count = 0
# while count < 10:
#     count = count + 1
#     if count == 5:
#         continue
#     if count == 6:
#         break
#     print(count)

# For loop
sample = ["server1", "server2", "server3", "server4"]

# membership operator: 'in'
# value = "server1" in sample
# print(value)

# Use case 1: Print all elements inside a list
# for val in sample:
#     print(val)

# Use case 2: Print all elements inside a list along with its index
# enumerate, range

# print(list(enumerate(sample)))

# for idx, value in enumerate(sample):
#     print(idx, value)

# print(list(range(1, 11, 2))) # print all the odd numbers starting from 1 till 10 (not included)

# sample = ["server1", "server2", "server3", "server4"]
# for idx in range(len(sample)):
#     print(idx, sample[idx])

# Please go through these concepts: Lazy execution, Generators and iterators

# Tuple unpacking
a, b = (1, 2)
print(a, b)

# List unpacking
a, b = [1, 2]
print(a, b)
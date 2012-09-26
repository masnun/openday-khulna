id_list = [1,2,3,4,5,6,7,8,9,10]
# Indexing
print id_list[1]
# Add to list
id_list.append(11)
print id_list
# Remove from list
id_list.remove(11)
print id_list
# Slicing
new_list = id_list[0:2]
print new_list
# List Comprehension
another_list = [x for x in id_list if x > 5]
print another_list
# All those squares!
print [x**2 for x in id_list]

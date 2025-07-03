# Sets

#   UNORDERED series of values. Duplicate values are NOT allowed.
#   Values in Sets are IMMUTABLE!! They CANNOT be edited!
#   HOWEVER, values can be added or removed.
#   Sets are declared in curly brackets {}.
#   Used when working with collections of unique elements, e.g.,
#   removing duplicates from lists or checking membership

my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)  #   Fxn {.add()} adds a value to the end of a set.

my_set.remove(4)  #   Fxn {.remove()} removes a SPECIFIC value from a set.
print(my_set)

#   Union (combines sets), Intersection (finds common elements), Difference (finds unique elements)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#   Union
union_set = set1.union(set2)
print(union_set)    #   Fxn {.union()} combines two Sets together and removes duplicate data.

#   Intersection
common_set = set1.intersection(set2)
print(common_set)   # Fxn {.intersection()} evaluates two Sets and stores only the common elements.

#   Difference
unique_set = set1.difference(set2)
print(unique_set)
#   Fxn {set1.difference(set2)} evaluates the contents of Set1 relative to Set2,
#   and stores ONLY the values that are UNIQUE to Set1!!


# Tuple

#   Ordered series of values. Duplicate values are allowed.
#   Tuple values are IMMUTABLE!! They CANNOT be edited!
#   Tuples are declared in round brackets ().
#   Used to store data that SHOULD NOT be edited by user or code,
#   e.g., coordinates, RGB values, database trackers.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print()

print(my_tuple[0])  #   Tuples are zero-indexed  ∴ my_tuple[0] refers to "1"
print(my_tuple[2])
print(my_tuple[-2])
#   Can use "negative-indexing" to call values from the end of the list.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concat_tuple = tuple1 + tuple2
print(concat_tuple)  #   Tuples and Lists can be CONCATONATED together

rep_tuple = tuple1 * 3
print(rep_tuple)  #   Tuples and Lists can be REPEATED

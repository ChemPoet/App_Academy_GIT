#Dictionary

#   Python Dictionary == Collection of key value pairs
#   Can be indexed using strings or numbers.
#   Entries are mutable (can be edited).

#   Dictionaries are defined within curly braces. Each entry is defined as a {KEY: Value} pair

my_dict = {'apple': 3, 'banana': 5, 'orange': 2}
#         {key: value}

print(my_dict['apple'])
#   Dictionary VALUES are accessed by calling the KEY in square brackets.

my_dict['grapes'] = 4
#   Add new entry to dictionary using square brackets, specifying the new KEY and value.
print(my_dict)

my_dict['banana'] = 7
#   Reusing the same KEY with a new VALUE overrides the previously saved KEY:Value pair.
print(my_dict)
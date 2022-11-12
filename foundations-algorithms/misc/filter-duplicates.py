# use a hashtable (dict) to filter out duplicate items
# linear algo


# define a set of items where we want to remove duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable (dict) to perform a filter
filter = dict()

# TODO: loop over each item and add to the dict with a value of 0
for key in items:
    filter[key] = 0
    print(filter)

# TODO: create a set from the resulting keys in the dict
result = set(filter.keys())
print(result)
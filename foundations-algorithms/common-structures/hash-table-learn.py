items1 = dict({"key 1":1, "key 2":2, "key 3": "three"}) #no guaranteed order
print(items1)

items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

#nonexistent key
#print(items1["key6"])

items2["key2"] = "two"
print(items2)

#iteration
for key, value in items2.items():
    print(key, ":", value)
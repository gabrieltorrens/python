# Linear big O : O(n)

items = [6, 1, 3, 2, 5, 4]

def find_item(item, itemlist):
    for i in range(0,len(items)):
        if item == itemlist[i]:
            return i
    return None

print(find_item(77, items))
print(find_item(3, items))

# determine if a list is sorted


items1 = [1,2,3,4,5,6]
items2 = [1,3,5,2,4,6]

def is_sorted(itemlist):
    #all function, check if "itemlist[i] <= itemlist[i+1]" is always true
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))
    
    # TODO: using the brute force method
    # for i in range(0,len(itemlist)-1):
    #     if (itemlist[i] > itemlist[i+1]):
    #         return False
    # return True

print(is_sorted(items1))
print(is_sorted(items2))


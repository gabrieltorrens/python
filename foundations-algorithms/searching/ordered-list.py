def binarysearch(item,itemList):
	lowerIndex = 0
	upperIndex = len(itemList)-1
	found = False
	while( lowerIndex<=upperIndex and not found):
		mid = (lowerIndex + upperIndex)//2
		if itemList[mid] == item :
			found = True
		else:
			if item < itemList[mid]:
				upperIndex = mid - 1
			else:
				lowerIndex = mid + 1	
	return found

myList = [1,2,3,4,5,6]

print(binarysearch(2, myList))
print(binarysearch(5, myList))

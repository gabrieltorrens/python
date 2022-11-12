#merge sort (with recursion)
#log time O(n log n)

items = [6, 2, 3, 4, 1, 5]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2 #make two arrays
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        # print("breaking leftarr=",leftarr)
        # print("breaking rightarr=",rightarr)

        # TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)
        # print("leftarr=",leftarr)
        # print("rightarr=",rightarr)
        
        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while i< len(leftarr) and j< len(rightarr):
            if leftarr[i] < rightarr[j]:
                # print("leftarr[i]=",leftarr[i])
                dataset[k] = leftarr[i]
                i+=1
            else:
                # print("rightarr[j]=",rightarr[j])
                dataset[k] = rightarr[j]
                j+=1
            k+=1

        # TODO: if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i+=1
            k+=1

        # TODO: if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j+=1
            k+=1


# test the merge sort with data
print(items)
mergesort(items)
print(items)

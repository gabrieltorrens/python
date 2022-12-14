def bubbleSort(dataset):
    # TODO: start with the array length and decrement each time
    for i in range(len(dataset)-1,0,-1): #countdown from end of array
        for j in range(i): #for loop in a for loop usually = quadratic big O, O(n^2)
            if dataset[j] > dataset[j+1]: #swap place if looking at a bigger number
                temp = dataset[j] #move bigger num to a temp var
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp #move bigger num to j+1
    
        print("Current state: ", dataset)


def main():
    list1 = [9, 333, 55, 2, 88, 23, 63, 41, 6, 53, 1]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()

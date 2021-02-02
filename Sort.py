class Sort:
    # constructor/ initializer
    def __init__(self):
        print(self)

    @staticmethod
    def bubbleSort(data):
        swaps = 0
        # Size of Array
        size = len(data)
        i = 0
        while i < size-1:
            j = 0
            while j < size-i-1:
                if data[j] > data[j+1]:
                    # swap two elements
                    data[j], data[j+1] = data[j+1], data[j]
                    swaps = swaps + 1
                j=j+1
            i=i+1
        print(f"Steps: {i} \t Swaps: {swaps}")
        return data

    @staticmethod
    def selectionSort(data):
        # Size of Array
        size = len(data)
        swaps = 0

        i = 0
        while i < size-1:
            currentMinIndex = i
            j = i + 1
            while j <= size-1:
                if data[j] < data[currentMinIndex]:
                    currentMinIndex = j
                j = j + 1
            # swap
            if i != currentMinIndex:
                data[i], data[currentMinIndex] = data[currentMinIndex], data[i]
                swaps = swaps + 1
            i = i + 1
        print(f"\nSteps: {i} \t Swaps: {swaps}")
        return data

    def myfunc():
        print(f"Hello!")


a = [10,9,8,7,6,5,4,3,2,1,0]
print(f"Unsorted Array is: {a}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
# a.copy() makes a copy of list a and then passes to the function. Otherwise functions overwrites the same list.
print(f"Sorted Array using Bubble Sort is: {Sort.bubbleSort(a.copy())}")
print(f"Sorted Array using Selection Sort is: {Sort.selectionSort(a.copy())}")
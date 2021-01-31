class Sort:
    # constructor
    def __init__(self):
        print(self)

    @staticmethod
    def bubbleSort(arr):
        swaps = 0
        # Size of Array
        size = len(arr)
        i = 0
        while i < size-1:
            j = 0
            while j < size-i-1:
                if arr[j] > arr[j+1]:
                    # swap two elements
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps = swaps + 1
                j=j+1
            i=i+1
        print(f"Steps: {i} \t Swaps: {swaps}")
        return arr

    @staticmethod
    def selectionSort(arr):
        # Size of Array
        size = len(arr)
        swaps = 0

        i = 0
        while i < size-1:
            j = i + 1
            while j <= size-1:
                if arr[i] > arr[j]:
                    # swap
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps = swaps + 1

                j = j + 1
            i = i + 1
        print(f"Steps: {i} \t Swaps: {swaps}")
        return arr

    def myfunc():
        print(f"Hello!")


a = [2,6,9,4,8,1,5,10]
print(f"Unsorted Array is: {a}")
# a.copy() makes a copy of list a and then passes to the function. Otherwise functions overwrites the same list.
print(f"Sorted Array using Bubble Sort is: {Sort.bubbleSort(a.copy())}")
print(f"Sorted Array using Selection Sort is: {Sort.selectionSort(a.copy())}")
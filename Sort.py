class Sort:
    # constructor
    #def __init__(self,name):
     #   self.name = name

    def bubbleSort(self, arr):
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

    def myfunc():
        print(f"Hello!")

obj = Sort()
a = [2,6,9,4,8,1,5,7]
sorted_a = obj.bubbleSort(a)
print(f"Sorted Array is: {sorted_a}")

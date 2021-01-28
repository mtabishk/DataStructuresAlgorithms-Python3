# Sorting Algorithm: Bubble Sort
# Time Complexity: O(n^2) , where n is the no of elements
# Space Complexity: O(1)
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


#arr = [2,6,9,4,8,1,5,7]
arr = list(range(999999,0,-1))
sorted_arr = bubbleSort(arr)
print(f"Sorted Array is: {sorted_arr}")
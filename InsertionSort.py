# Sorting Algorithm: Insertion Sort
# Time Complexity: O(n^2) , where n is the no of elements
# Space Complexity: O(1)

def insertionSort(arr):
    print(f"Unsorted Array: {arr}")
    # Size of Array
    size = len(arr)
    swaps = 0
    i = 1
    while i <= size-1:
        temp = i
        j = i-1
        while j >= 0:
            if arr[temp] < arr[j]:
                # swap
                arr[temp], arr[j] = arr[j], arr[temp]
                swaps = swaps + 1
                temp = j
            j = j - 1
        i = i + 1
        print(f"{arr}")
    print(f"Steps: {i} \t Swaps: {swaps}")
    return arr

a = [2,6,9,4,8,1,5,7]
sorted_arr = insertionSort(a)
print(f"Sorted Array is: {sorted_arr}")
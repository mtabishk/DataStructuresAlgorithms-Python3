# Sorting Algorithm: Insertion Sort
# Time Complexity: O(n^2) , where n is the no of elements
# Space Complexity: O(1)

def insertionSort(arr):
    # Size of Array
    size = len(arr)
    swaps = 0

    i  = 1
    while i < size:
        current = arr[i]
        j = i-1
        while j >= 0:
            if current < arr[j]:
                current, arr[j] = arr[j], current
                swaps+=1
            j-=1
        i+=1
    print(f"Steps: {i} \t Swaps: {swaps}")
    return arr

a = [2,6,9,4,8,1,5,7]
sorted_arr = insertionSort(a)
print(f"Sorted Array is: {sorted_arr}")
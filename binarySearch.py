# Binary Search Algorithm
# Time Complexity: O(logn)
def binary_search(arr, item):
    start = 0
    end = len(arr) - 1

    steps = 0
    while start <= end:
        steps = steps + 1
        middle = (start + end) // 2

        if item == arr[middle]:
            print(f"Item {item} found at index {middle} in {steps} steps")
            return
        elif item < arr[middle]:
            end = middle - 1
        elif item > arr[middle]:
            start = middle + 1
    else: 
        print(f"Item {item} not found in {steps} steps")


db = list(range(1,99999999))
binary_search(db, 99999998)
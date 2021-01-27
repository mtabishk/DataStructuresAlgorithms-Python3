# Linear Search or Sequential Search Algorithm
# Time Complexity: O(n)
def sequential_search(arr, item):
    pos = 0
    found = False

    steps = 0
    while pos < len(arr) and not found:
        steps = steps + 1
        if arr[pos] == item:
            found = True
            print(f"Element found at position: {pos} in {steps} steps")
            break
        else:
            pos+=1
    return found
        
#a = [10,20,6,-11,22,45,76]
#element = int(input("Enter the element: "))
#print(sequential_search(a, element))
a = list(range(1,99999999))
print(sequential_search(a,99999998))

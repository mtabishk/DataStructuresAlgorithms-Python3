# Linear Search or Sequential Search Algorithm
# Time Complexity: O(n)
def sequential_search(arr, item):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == item:
            found = True
            print(f"Element found at position: {pos}")
            break
        else:
            pos+=1
    return found
        
#a = [10,20,6,-11,22,45,76]
#element = int(input("Enter the element: "))
#print(sequential_search(a, element))
a = list(range(1,99999999))
sequential_search(a,99999998)

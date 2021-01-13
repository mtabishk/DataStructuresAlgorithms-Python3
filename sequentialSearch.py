# Linear Search or Sequential Search Algorithm
# Time Complexity: O(n)
def sequential_search(arr, item):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == item:
            found = True
            print("Element found at position: {}".format(pos))
            break
        else:
            pos+=1
    return found
        
a = [10,20,6,-11,22,45,76]
element = int(input("Enter the element: "))
print(sequential_search(a, element))

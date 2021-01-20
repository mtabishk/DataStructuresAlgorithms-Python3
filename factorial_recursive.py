# Factorial of a number recursively
# Time Complexity: O(n)
def factorial_recv(num):
    # edge cases
    if num < 0 or int(num) != num:  # int(num) != num : to check if the number is int
        return "Not Supported !"
    
    # base case
    if  num == 1 or num == 0: 
        return 1
    
    # recursive call 
    return num * factorial_recv(num-1)

try:
    n = int(input("Enter the number: "))
    print(factorial_recv(n))
except Exception as e:
    print(f"{e}  \nNot Supported!")

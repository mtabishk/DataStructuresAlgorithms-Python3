# Factorial of a number recursively
# Time Complexity: O(n)
def factorial_recv(num):
    # base case
    if  num == 1 or num == 0: return 1
    return num * factorial_recv(num-1)

n = int(input("Enter the number: "))
print(factorial_recv(n))
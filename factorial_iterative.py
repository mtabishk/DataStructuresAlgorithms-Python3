# Factorial of a number iteratively
# Time Complexity: O(n)
def factorial_iter(num):
    if num == 0 or num == 1: return 1
    fac = 1
    while num > 1:
        fac = fac * num
        num = num - 1

    return fac

n = int(input("Enter the number: "))
print(factorial_iter(n))


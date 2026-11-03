# Fibonacci using Recursive and Non-Recursive methods

count = 0

# Recursive function
def recursive_fibonacci(n):
    global count
    count = count + 1

    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


# Non-Recursive function
def non_recursive_fibonacci(n):
    a = 0
    b = 1
    steps = 0

    print("Non-Recursive Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        steps = steps + 1

    print("\nStep Count:", steps)


# Main program
n = int(input("Enter the number of terms: "))

# Non-Recursive
non_recursive_fibonacci(n)

# Recursive
print("\nRecursive Fibonacci Series:")
count = 0

for i in range(n):
    print(recursive_fibonacci(i), end=" ")

print("\nStep Count:", count)
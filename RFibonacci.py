count = 0

def fibonacci(n):
    global count
    count = count + 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")

print("\nStep Count:", count)
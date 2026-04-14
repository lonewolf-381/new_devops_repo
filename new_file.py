print("Hello, Welcome to my Python World")
print()
num = int(input("Enter the number of repeats: "))
current = 0
next_val = 1
print("1.", current)
print("2.", next_val)
for i in range(3, num):
    fib = current + next_val
    print(f"{i}.", fib)
    current = next_val
    next_val = fib

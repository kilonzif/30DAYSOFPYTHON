n = int(input("Enter a positive integer: "))

fibonacci = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers

for i in range(2, n):
    next_num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_num)

print(f"Fibonacci numbers up to {n}:")
print(fibonacci[:n])
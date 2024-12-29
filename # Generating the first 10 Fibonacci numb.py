# Generating the first 10 Fibonacci numbers
n = 10  # Number of Fibonacci numbers to generate
fibonacci_sequence = []

# Initial two numbers of the Fibonacci sequence
a, b = 0, 1

for _ in range(n):
    fibonacci_sequence.append(a)
    a, b = b, a + b

print("The first 10 Fibonacci numbers are:", fibonacci_sequence)

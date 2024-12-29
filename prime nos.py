n = int(input("Enter a number: "))
print("Prime numbers from 1 to", n, "are:")

for num in range(2, n + 1):  # Iterate through each number from 2 to n
    ctr = 0
    for i in range(1, num + 1):  # Check divisors of the current number
        if num % i == 0:
            ctr += 1
    if ctr == 2:  # If the number has exactly two divisors, it's prime
        print(num, end=" ")  # Print the prime number

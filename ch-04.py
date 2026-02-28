#loop in python
#for loop
for i in range(1, 11):
    print(i)

#while loop

count = 0
while count < 5:
    print("Count:", count)
    count += 1

# nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")


# practice problem: print the multiplication table of a given number
number = 5
print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
# practice problem: print the Fibonacci sequence up to a given number of terms
terms = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(terms):
    print(a, end=' ')
    a, b = b, a + b

# practice problem: print all prime numbers up to a given number
limit = 20
print(f"Prime numbers up to {limit}:")
for num in range(2, limit + 1):
    is_prime = True
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

# practice problem: print the factorial of a given number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
number = 5
print(f"Factorial of {number} is {factorial(number)}")


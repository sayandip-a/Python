# conditionals
x = 10
if x > 0:
    print("x is positive")

y = -5
if y < 0:
    print("y is negative")

# if-else statement
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else statement
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# nested if-else statements
num = 15
if num > 0:
    if num % 2 == 0:
        print("num is a positive even number")
    else:
        print("num is a positive odd number")
else:
    print("num is not positive")

# ternary operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# logical operators in conditionals
is_raining = True
is_cold = False
if is_raining and is_cold:
    print("It's a rainy and cold day.")
elif is_raining and not is_cold:
    print("It's a rainy but not cold day.")
elif not is_raining and is_cold:
    print("It's a cold but not rainy day.")
else:
    print("It's a nice day.")

# practice problem: check if a number is prime
# a prime number is a number greater than 1 that has no divisors other than 1 and itself
# write a program to check if a number is prime or not
# practice problem: check if a number is even or odd
# write a program to check if a number is even or odd
# practice problem: check if a year is a leap year
# a leap year is a year that is divisible by 4 but not by 100, or it is divisible by 400
# write a program to check if a year is a leap year or not
# practice problem: check if a string is a palindrome
# a palindrome is a string that reads the same backward as forward
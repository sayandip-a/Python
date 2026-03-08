#function in python 

def greet():
    print("hello world")

greet()

#function with parameters and args

def add(a,b):
    print(f"The sum of a+b is:{a+b}")
add(2,8)

# deafult args
def hello(name,age=21):
    print(f"My name is {name} and my age is {age}")

hello( name="sayandip")

def sum(a,b=24):
    print(f"The sum is {a+b}")

sum(4)

#keyword args 

def info(name,age):
    print(f"My name is {name} and my age is {age}")

info(name="sayandip",age=21)


#write a function to cheack palindrome

def check_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
word = input("Enter a word: ")

if check_palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")

#function with return keyword

def printhello():
    return "hello world"

print(printhello())
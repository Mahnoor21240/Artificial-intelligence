# 1. Find numbers divisible by 7 and multiple of 5, between 1500 and 2700
def find_numbers():
    numbers = [x for x in range(1500, 2701) if x % 35 == 0]
    return numbers

print("Numbers divisible by 7 and multiple of 5:", find_numbers())
# 2. Convert temperatures between Celsius and Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("60°C is", celsius_to_fahrenheit(60), "in Fahrenheit")
print("45°F is", fahrenheit_to_celsius(45), "in Celsius")
# 3. Guess a number between 1 to 9
import random

def guess_number():
    number_to_guess = random.randint(1, 9)
    while True:
        user_guess = input("Guess a number between 1 and 9: ")
        try:
            user_guess = int(user_guess)
            if user_guess < 1 or user_guess > 9:
                print("Please enter a number between 1 and 9.")
                continue
            if user_guess == number_to_guess:
                print("Well guessed!")
                break
            else:
                print("Wrong guess, try again!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

guess_number()

# 4. Construct a pattern using nested for loop
def print_pattern():
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

print_pattern()
# 5. Reverse a word provided by the user
def reverse_word():
    word = input("Enter a word: ")
    return word[::-1]

print("Reversed word:", reverse_word())
# 6. Count the number of even and odd numbers from a series of numbers
def count_even_odd(numbers):
    even_count = len([x for x in numbers if x % 2 == 0])
    odd_count = len([x for x in numbers if x % 2 != 0])
    return even_count, odd_count

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count, odd_count = count_even_odd(numbers)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
# 7. Print each item and its corresponding type from a list
def print_list_types(datalist):
    for item in datalist:
        print(item, type(item))

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {'class': 'V', 'section': 'A'}]
print_list_types(datalist)
# 8. Print numbers from 0 to 6 except 3 and 6
def print_numbers():
    for num in range(7):
        if num == 3 or num == 6:
            continue
        print(num, end=' ')

print_numbers()
print()
 # 9. Get the Fibonacci series between 0 to 50
def fibonacci_series():
    a, b = 1, 1
    while a <= 50:

        print(a, end=' ')
        a, b = b, a + b

fibonacci_series()
print()
# 10. Print "FizzBuzz" for multiples of 3 and 5
def fizzbuzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
# 11. Generate a two-dimensional array based on given rows and columns
def generate_array(m, n):
    array = [[i * j for j in range(n)] for i in range(m)]
    return array

rows, cols = 3, 4
print("Generated array:", generate_array(rows, cols))
# 12. Accept a sequence of lines and print them in lower case
def print_lines():
    lines = []
    while True:
        line = input("Enter a line (blank line to terminate): ")
        if line == "":
            break
        lines.append(line.lower())
    for line in lines:
        print(line)

print_lines()
# 13. Print binary numbers divisible by 5
def binary_divisible_by_5(binary_numbers):
    divisible_by_5 = [num for num in binary_numbers if int(num, 2) % 5 == 0]
    return ','.join(divisible_by_5)

binary_numbers = input("Enter binary numbers separated by commas: ").split(',')
print("Binary numbers divisible by 5:", binary_divisible_by_5(binary_numbers))
 # 14. Count the number of digits and letters in a string
def count_digits_letters(s):
    digits = sum(c.isdigit() for c in s)
    letters = sum(c.isalpha() for c in s)
    return letters, digits

s = "ARZU 03 MAY"
letters, digits = count_digits_letters(s)
print("Letters:", letters)
print("Digits:", digits)
# 15. Check the validity of a password
import re

def check_password(password):
    if (6 <= len(password) <= 16 and
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[$#@]', password)):
        return True
    return False

password = input("Enter a password: ")
if check_password(password):
    print("Password is valid")
else:
    print("Password is invalid")
    print()
# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

birth_year = input('Enter your birth year ')
age = 2023 - int(birth_year)
print(age)
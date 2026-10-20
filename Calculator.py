# Simple console calculator script

print("Simple Calculator - LarvaMonkey")
first_number = input("First number: ")

while not first_number.isdigit(): # Check if input is a number.
	print("Please only input numbers for this question")
	first_number = input("First number: ")

second_number = input("Second number: ")

while not second_number.isdigit(): # Check if input is a number.
	print("Please only input numbers for this question")
	second_number = input("Second number: ")

# Convert both input's from a string into an integer.
first_number = int(first_number)
second_number = int(second_number)

symbol = input("Please provide the symbol you'd like to use: ")

while symbol not in ["x", "+", "/", "-"]: # Check if input includes a supported symbol.
	print("Please use the supported symbols: x, +, /, or -")
	symbol = input("Please provide the symbol you'd like to use: ")

# ima continue this tmrw, it's 1am and lowk I'm tired, hungry, and bored.
# Made by LarvaMonkey.
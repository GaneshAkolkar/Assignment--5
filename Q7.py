# Write a python script which takes a three digit number from the user and displays
# only its last digit.

# Take input from user for a three-digit number
number = input("Enter a three-digit number: ")

# Extract the last digit of the number
last_digit = number[2]

# Print the last digit
print("The last digit of", number, "is", last_digit)

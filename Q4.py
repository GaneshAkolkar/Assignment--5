# Write a python script to find x power y, where values of x and y are given by user

# Take input from user for values of x and y
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

# Calculate x to the power of y using the pow() function
result = pow(x, y)

# Print the result
print(x, "to the power of", y, "is", result)

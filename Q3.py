# Take input from user for variables a and b
a = input("Enter value of a: ")
b = input("Enter value of b: ")

# Print the original values of a and b
print("Before swapping, a =", a, "and b =", b)

# Swap the values of a and b using a temporary variable
temp = a
a = b
b = temp

# Print the new values of a and b after swapping
print("After swapping, a =", a, "and b =", b)

# Write a python script to use IS operator to display if both variables are the same
# object or not?

x = [1, 2, 3]
y = [1, 2, 3]

# Check if x and y refer to the same object
if x is y:
    print("x and y refer to the same object.")
else:
    print("x and y do not refer to the same object.")

# Define two variables referring to the same object
a = [4, 5, 6]
b = a

# Check if a and b refer to the same object
if a is b:
    print("a and b refer to the same object.")
else:
    print("a and b do not refer to the same object.")

num_str = input("Enter a number: ")
num_str = num_str[:-1] # removes last digit from string
num = int(num_str) # converts string back to integer
print("Number without last digit:", num)

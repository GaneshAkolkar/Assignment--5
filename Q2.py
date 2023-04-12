# */Write a python script to get the last digit from a given number. (for example, if user
# enters 2089 then your output should be 9)
number = int(input("Enter a number: "))
last_digit = number % 10
print("The last digit of", number, "is", last_digit)

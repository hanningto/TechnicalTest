'''Write a program that takes an integer as input and returns true if the input is a power of two.'''

number = int(input("Enter an integer: "))# take user input

# checks if number is a power of 2
if number > 0 and (number & (number - 1)) == 0:
    result = True
else:
    result = False

print(result)#prints results

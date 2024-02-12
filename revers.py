'''Write a program that takes an integer as input and returns an integer with reversed digit
ordering.'''

number = int(input("Enter a number: "))
if number < 0:
    sign = -1
else:
    sign = 1

rev_number = int((str(abs(number))[::-1])) * sign

print(rev_number)
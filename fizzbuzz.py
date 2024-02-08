'''Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
"FizzBuzz".'''


for i in range(101): #iterate from 1-100

    #check for divisibility by both 3 and 5
    if i%3 == 0:# check for divisibility by 3
        if i%5 == 0:
            print("FizzBuzz")
            continue #continue with the loop
        print("fizz")
        continue

    #check for divisibility by 5
    if i%5 == 0:
        print("buzz")
        continue

    print(i) # prints the rest of the numbers that are not divisible by 3 or 5
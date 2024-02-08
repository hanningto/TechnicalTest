'''Write a program to generate the Fibonacci sequence up to 100.'''
#Create a list to hold the fibonacci numbers
holder = [0, 1]#start with 0 and 1 in the list
for i in range(0, 10):#iterate 10 times so as to stay within the range of 100
    sum = holder[-2] + holder[-1]#add the last 2 numbers in the sequence
    holder.append(sum)# add the sum to the list

print(holder) # print the list

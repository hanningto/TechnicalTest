'''Write a program that counts the number of vowels in a sentence.'''

vowels = ['a','e','i','o','u']# initialize the vowels

stat = input("Enter a sentence: ")# get the sentence
found = []# initialize an empty list where the vowels in the sentence will be stored

#iterate through the two variables to find and store the vowels found
for i in stat:
    for x in vowels:
        if i == x:
            
            found.append(i)# add found vowel to the list

print(len(found))# count and print the number of elements within the found list

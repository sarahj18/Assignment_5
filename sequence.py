# first = 0
# second = 0
# third = 1
# ask for sequence number
# for-lykkja from 0 to sequence number 
# prints out the sequence
# algorithm is as such;
# number is addition of the last three numbers 
# 1, 2, 3, 6, 11, 20, 37, 68, 125.. m
# new number is printed out called next number
# third number than takes value of the next number
# second takes value of the third
# first number takes value of the second 

n = int(input('Enter the length of the sequence: '))

first = 0
second = 1
third = 2

for i in range(0,n):
    if i == 0:
        print(second) # print out 1 for first number in sequence
    elif i == 1:
        print(third) # print out 2 for second number in sequence
    else:
        #now i calculate next numbers
        next_number = first + second + third
        first = second
        second = third
        third = next_number
        print(next_number)
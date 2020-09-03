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

first = 1
second = 2
third = 3

for i in range(0,n):
    if i == 0:
        print(first)
    elif i == 1:
        print(second)
    elif i == 2:
        print(third)
    else:
        next_number = first + second + third
        first = second
        second = third
        third = next_number
        print(next_number)
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

first = 0
second = 0
third = 1

n = int(input('Enter the length of the sequence: '))

for i in range(0,n):
    next_number = first + second + third
    third = next_number, second = third, first = second
    print(next_number, end=' ')
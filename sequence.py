# A program that asks for a sequence number,b, and prints out a sequence, n times.
# ask for a sequence number
# 1 and 2 are printed out right away if the sequence is longer
# then three numbers
# the next number is an addition from the last three numbers
# the next number is then printed out
# 1, 2, 3, 6, 11, 20, 37, 68, 125.. m
# the values of the first three numbers change
# the first number takes the value of the second
# the second of the third
# the third of the next number
# the numbers of the sequence are printed until the sequence has n numbers.

n = int(input('Enter the length of the sequence: '))

first = 0
second = 1
third = 2

# printing out each number from the sequence until the limit, n, is reached
for i in range(0,n):
    if i == 0:
        print(second) # print out 1 for first number in sequence
    elif i == 1:
        print(third) # print out 2 for second number in sequence
    else:
        #now calculate the next numbers in the sequence
        #to be printed out
        next_number = first + second + third
        first = second
        second = third
        third = next_number
        print(next_number)
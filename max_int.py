# Ask for a number
# Assign value 0 to variable max_int which is maximum input 
# in beginning
# If input is negative in the beginning we ask again for a new input
# If input is larger than maximum input it becomes the new maximum input
# If input is smaller than maximum input the maximum input stays the same
# ask for another number
# If the input is negative we stop and print out the maximum input value

num_int = int(input=("Input a number: "))
max_int = 0
# if the number is negative in the beginning
while num_int < 0:
    num_int = int(input("Input a number: "))

while num_int > 0:
    if max_int < num_int: # if the new input is larger than 
        #it beomes the new value
        max_int = num_int
    num_int = int(input("Input a number: "))


print("The maximum is: ", max_int)
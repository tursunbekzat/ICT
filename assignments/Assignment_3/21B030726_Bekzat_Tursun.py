number = int(input("Enter a number between 1 and 10 (or 0 to exit): \n"))
sum = 0
while(number != 0):
    if 10 < number or number < 0: print("Sorry, if the number is not between 0 and 10 it's too hard for me")
    else: 
        sum += number
        print("The sum of all your number is:", sum)
    number = int(input("Enter a number between 1 and 10 (or 0 to exit): \n"))
print("The program is finished, the final sum is:", sum)
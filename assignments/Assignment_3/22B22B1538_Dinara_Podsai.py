num = int(input("Enter a number between 1 and 10 (or 0 to exit): \n"))
summa = 0
while(num != 0):
    if num < 0 or num > 10: print("Sorry, if the number is not between 0 and 10 it's too hard for me")
    else: 
        summa += num
        print("The sum of all your number is:", summa)
    num = int(input("Enter a number between 1 and 10 (or 0 to exit): \n"))
print("The program is finished, the final sum is:", summa)
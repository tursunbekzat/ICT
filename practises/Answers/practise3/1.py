age = int(input("Enter your age: "))
# first method
if age >= 18: print("Your are an adult.")
else: print("Your are a child.")

# second method
# print("Your are an adult." * (age>=18), end='')
# print("Your are a child." * (age<18), end='')
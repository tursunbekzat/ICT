a, b = int(input("Enter a number: ")), int(input("Enter a number: "))
if a % b == 0:
    print("Yes,", a, "is a nultiple of", a/b, "because", a/b, "*", b, "=", a)
else:
    print("No", a, "is not a multiple of", b, ".")
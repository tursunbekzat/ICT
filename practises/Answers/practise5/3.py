width = int(input("Enter the width of the pyramid: "))
for i in range(1, width // 2 + 2):
        print(' ' * (width - i) + '*' * i + '*' * (i - 1))
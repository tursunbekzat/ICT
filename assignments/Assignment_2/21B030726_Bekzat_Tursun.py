height = int(input("Height of the pyramid: "))
character = input("Character: ")

for i in range(height):
    if i == 0: print(' ' * (height-1), character, sep='')
    elif i == 1: print(' ' * (height - i - 2), '/ \\')
    elif i == height - 1: print('/', '_'*(height*2-3), '\\', sep='')
    else: print(' ' * (height - i - 2), '/', ' ' * (i * 2 - 3), '\\')